# -*- coding: utf-8 -*-
import os
import urllib2
import re
from xml.dom import minidom
import logging

logging_msg = """------------- %s -------------
%s
-------------------------------"""

logging.basicConfig(format="%(message)s", filename='error.log', 
                        filemode = "w", level = logging.ERROR)

url_xml_format = "http://www.boletinoficial.gob.ar/Content/Xml/Avisos/01/{0}/{1}/{2}/{3}.xml"
os.chdir("./txts") #Cambiar para que se le pueda pasar el directorio por commando
boletines = 0
for filename in os.listdir('.'):
    if filename.endswith("txt"):
        avisos_ids_regex = re.compile("#I(\d*)I#",re.MULTILINE | re.UNICODE)

        with open(filename, 'r') as boletin_file:
            boletin_str = boletin_file.read()
            avisos_ids = set(avisos_ids_regex.findall(boletin_str))

            ano = filename[:4]
            mes = filename[4:6]
            dia = filename[6:8]			
            for aviso_id in avisos_ids:
                try:
                    url_xml = url_xml_format.format(ano, mes, dia, aviso_id)
                    sock = urllib2.urlopen(url_xml)
                    dir_name = ano+mes+dia
                    if not os.path.isdir(dir_name):
                        os.mkdir(dir_name)
                    aviso_xml_str = sock.read()
                    xmldoc = minidom.parseString(aviso_xml_str)
                    aviso_tipo = xmldoc.getElementsByTagName('Tipo')
                    if aviso_tipo:
                            aviso_tipo_name = aviso_tipo[0].firstChild.data
                    else:
                            aviso_tipo_name = u"sin_tipo"

                    filename_xml = u"./{0}/{1}_{2}.xml".format(dir_name, aviso_tipo_name.lower(), aviso_id)
                    with open(filename_xml, 'w') as aviso_xml_file:
                            aviso_xml_file.write(aviso_xml_str)
                    print url_xml, ": ok"
                    boletines += 1
                except Exception, e:                
                    print url_xml, ": error"
                    logging.error(logging_msg, filename, url_xml)

print boletines
