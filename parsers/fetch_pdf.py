import sys
import os
import requests
import time
import datetime
import logging
import re
import MySQLdb
from primera_seccion import designaciones_db
from tercera_seccion import adjudicaciones_parser
from xml.dom import minidom

PDF_PATH = 'pdf/'
TXT_PATH = 'txt/'
XML_PATH = 'xml/'
BO_URL = "http://www.boletinoficial.gov.ar/DisplayPdf.aspx?s={0}&f={1}"
BO_URL_XML = "http://www.boletinoficial.gob.ar/Content/Xml/Avisos/01/{0}/{1}/{2}/{3}.xml"

def download(date, path = PDF_PATH, sections = ('01', '02', '03'), until = None):
    """ Se baja el boletin en formato pdf del sitio oficial

        date: dia del boletin a bajar
        path: donde se guarda el boletin
        sections: secciones del boletin a bajar
        until: hasta que dia baja
        return: regresa una lista con los path de los tres boletines
    """
    if not until: until = date
    boletines = []
    delta = datetime.timedelta(days = 1)
    while date <= until:
        for section in sections:
            date_str = date.strftime('%Y%m%d')
            filename = '{0}-{1}.pdf'.format(date_str, section)
            filename_path = os.path.join(path, filename)
            print filename_path
            if not os.path.exists(filename_path):
                r = requests.get(BO_URL.format(section, date_str), timeout = 1)
                with open(filename_path, 'w') as f:
                    f.write(r.content)
                    time.sleep(2)

            boletines.append(filename_path)
        date += delta
    return boletines

def parse_pdf(filename_path, output_path = TXT_PATH):
    """ Se parsea el pdf 

        filename_path: path/filename del pdf a parsear
        output_path: path donde se dejan los pdf parseados
        return: path/filename del pdf parseado
    """
    assert '.' in filename_path
    txts = []
    filename = os.path.basename(filename_path)
    filename_out = os.path.splitext(filename)[0] + ".txt"
    path_filename_out = os.path.join(output_path, filename_out)

    if not os.path.exists(path_filename_out):
        os.system('java -jar pdfbox-app-1.7.0.jar ExtractText -encoding UTF-8 {0} {1}'.format(filename_path, path_filename_out))

    return path_filename_out

def get_avisos_from_bo(filename_path):
    """ Obtenemos los ids de los avisos del boletin

        filename_path: path/filename del pdf a recorrer
        return: la fecha del boletin con sus avisos
    """
    with open(filename_path, 'r') as boletin_file:
        boletin_str = boletin_file.read()
        avisos_ids_regex = re.compile("#I(\d*)I#",re.MULTILINE | re.UNICODE)
        avisos_ids = set(avisos_ids_regex.findall(boletin_str))

        fecha = os.path.basename(filename_path)[0:8]
        return {fecha: avisos_ids}

def download_xml(avisos_id, output_path = XML_PATH):
    """ Baja los xmls para la primera seccion. 

        avisos_id: ids de los avisos a bajar
        output_path: path donde se dejan los xmls 
        return: el path de los xmls
    """
    xmls = []
    for fecha in avisos_id:
        dir_name = os.path.join(output_path, fecha)
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)

        ano = fecha[:4]
        mes = fecha[4:6]
        dia = fecha[6:8]			
        for aviso_id in avisos_id[fecha]:

            try:
                url_xml = BO_URL_XML.format(ano, mes, dia, aviso_id)
                r = requests.get(url_xml, timeout = 1)
                aviso_xml_str = r.content
                time.sleep(.5)

                xmldoc = minidom.parseString(aviso_xml_str)
                aviso_tipo = xmldoc.getElementsByTagName('Tipo')
                if aviso_tipo:
                        aviso_tipo_name = aviso_tipo[0].firstChild.data
                else:
                        aviso_tipo_name = u"sin_tipo"

                filename_xml = u"{0}_{1}.xml".format(aviso_tipo_name.lower(), aviso_id)
                filename_xml_path = os.path.join(dir_name, filename_xml)
                print filename_xml_path
                with open(filename_xml_path, 'w') as aviso_xml_file:
                        aviso_xml_file.write(aviso_xml_str)
                print url_xml, ": ok"

                xmls.append(filename_xml_path)
            except Exception, e:                
                return xmls
                print url_xml, ": error"
                #logging.exception('DOWNLOAD XML: %s %s', filename_path, url_xml)

    return xmls

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print >>sys.stderr, 'usage: download_pdf.py <from date: yyyymmdd> <to date: yyyymmdd>'
        sys.exit(2)

    #logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", filename='log', 
    #                 filemode = "a+")

    date = datetime.datetime.strptime(sys.argv[1], '%Y%m%d')
    date_to = date
    if len(sys.argv) == 3:
        date_to = datetime.datetime.strptime(sys.argv[2], '%Y%m%d')

    # Bajamos los pdfs
    pdfs = download(date, until = date_to)
    txts = {'1seccion' : [], '2seccion' : [], '3seccion' : []}

    # Parseamos los pdfs
    for pdf in pdfs:
        if pdf.find('03') > 0:
            seccion = '3seccion' 
        elif pdf.find('02') > 0:
            seccion = '2seccion' 
        else: 
            seccion = '1seccion'

        txts[seccion].append(parse_pdf(pdf))

    # De los pdfs parseados obtenemos los ids de los avisos
    # y bajamos los xmls correspondientes
    # NOTA: por el momento solo necesitamos los de la seccion 1
    xmls = {}
    for txt in txts['1seccion']:
        avisos_id = get_avisos_from_bo(txt)
        xmls[txt] = download_xml(avisos_id)

    # Populamos en la base de datos
    conn = MySQLdb.connect( host = '127.0.0.1', 
                            db = 'boletin_oficial',
                            user = 'banquito', 
                            passwd = 'banquito', 
                            charset = "utf8", 
                            use_unicode = True);

    cursor = conn.cursor()

    # Primera seccion
    for txt in xmls:
        if len(xmls[txt]) > 0:
            designaciones_db.popular_primera_seccion(xmls[txt], cursor)
 
    conn.commit()

    # Tercera seccion
    for txt in txts['3seccion']:
        with open(txt, 'r') as boletin_file:
            boletin_str = boletin_file.read()

        adjudicaciones_parser.parsea_boletin(boletin_str, cursor, txt)

    conn.commit()


    cursor.close()
    conn.close()

