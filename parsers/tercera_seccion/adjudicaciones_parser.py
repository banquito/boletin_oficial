# -*- coding: utf-8 -*-
from models import Adjudicacion, Boletin
import MySQLdb
import fixtures
import sys
import logging
import string
import os
import pprint
import datetime
import re

db_inserts = {'adjudicacion' :("INSERT INTO adjudicacion (objeto, texto_original, reparticion_id, boletin_id) VALUES(%s, %s, %s, %s)"),
              'reparticion' : "INSERT INTO reparticion (nombre) VALUES(%s)",
              'oferente'    : "INSERT INTO oferente (sociedad_id, adjudicacion_id, precio) VALUES(%s, %s, %s)",
              'sociedad'   : "INSERT INTO sociedad (nombre) VALUES(%s)",
              'sociedad2'   : "INSERT INTO sociedad2 (nombre) VALUES(%s)",
              'boletin'   : "INSERT INTO boletin (fecha, seccion) VALUES(%s, %s)" }

db_queries = {'sociedad' : "SELECT id FROM sociedad WHERE nombre = %s",
                'reparticion': "SELECT id FROM reparticion WHERE nombre LIKE %s"}

logging_msg = """------------- %s -------------
%s
-------------------------------"""

def parsea_boletin(boletin_str, cursor, filename = ""):
    boletin = Boletin(boletin_str)
    adjudicaciones_str = boletin.get_modulos_seccion("Adjudicaciones")
    totales = { "adjudicaciones" : 0, 
                "sociedades" : 0, 
                "oferentes" : 0,
                "reparticiones" : 0}

    boletin_regex = re.compile("-",re.IGNORECASE | re.MULTILINE)
    matchs = boletin_regex.split(filename)

    cursor.execute(db_inserts['boletin'], (matchs[0], matchs[1].replace('.txt', '')))
    boletin_id = cursor.lastrowid   

    for adjudicacion_str in adjudicaciones_str:
        adjudicacion = Adjudicacion(adjudicacion_str)
        
        reparticion = adjudicacion.get_entidad_publica()
        cursor.execute(db_queries['reparticion'], '%'+string.capwords(reparticion)+'%')
        reparticion_id = cursor.fetchone()

        if not reparticion_id:
            cursor.execute(db_inserts['reparticion'], reparticion)               
            totales['reparticiones'] += 1
            reparticion_id = cursor.lastrowid
        else:
            reparticion_id = reparticion_id[0]

        try:
            adjudicacion_objeto = adjudicacion.get_objeto()
            cursor.execute(db_inserts['adjudicacion'], 
                        (adjudicacion_objeto, 
                        adjudicacion.get_texto(),
                        reparticion_id,
                        boletin_id))
        except Exception, e:                
            logging.error(logging_msg, filename, adjudicacion.get_texto())

        adjudicacion_id = cursor.lastrowid         

        precios = adjudicacion.get_precios()
        proveedores = adjudicacion.get_proveedores()

        for proveedor, precio in zip(proveedores, precios):
            proveedor_title = string.capwords(proveedor)                
            cursor.execute(db_queries['sociedad'], proveedor_title)

            sociedad = cursor.fetchone()

            if not sociedad:
                cursor.execute(db_inserts['sociedad'], proveedor_title)                        
                totales['sociedades'] += 1
                proveedor_id = cursor.lastrowid
            else:
                proveedor_id = sociedad[0]

            #cursor.execute(db_inserts['sociedad2'], proveedor_title)                        
            
            precio_str = "{0} {1}".format(precio['moneda'], precio['valor'])
            cursor.execute(db_inserts['oferente'], 
                            (proveedor_id, adjudicacion_id, precio_str))

            totales['oferentes'] += 1

        totales['adjudicaciones'] += 1

    return totales

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print >>sys.stderr, 'usage: download_pdf.py <from date: yyyymmdd> <to date: yyyymmdd>'
        sys.exit(2)

    logging.basicConfig(format="%(message)s", filename='error.log', 
                        filemode = "w", level = logging.ERROR)

    filename_totales = {}

    os.chdir(sys.argv[2]) 
    conn = MySQLdb.connect( host = 'localhost', 
                            db = 'boletin_oficial',
                            user = 'clodo', 
                            passwd = 'cjbidau', 
                            charset = "utf8", 
                            use_unicode = True);

    cursor = conn.cursor()

    for filename in os.listdir('.'):
        if filename.endswith("txt"):
            with open(filename, 'r') as boletin_file:
                boletin_str = boletin_file.read()

            totales = parsea_boletin(boletin_str, cursor, filename)
            filename_totales[filename] =  totales

    conn.commit()
    cursor.close()
    conn.close()
