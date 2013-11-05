# -*- coding: utf-8 -*-
import MySQLdb
import os
import sys
from parsers import DecretoParser

def popular_primera_seccion(avisos_path, cursor):
    db_inserts = {'puesto'        : u"INSERT INTO puesto (nombre) VALUES(%s)",
                  'persona'       : u"INSERT INTO persona_2 (nombre, codigo_tipo, codigo_numero) VALUES(%s, %s, %s)",
                  'dependencia'   : u"INSERT INTO dependencia (nombre) VALUES(%s)",
                  'articulo'      : u"INSERT INTO articulo (texto) VALUES(%s)",
                  'designacion'  : u"INSERT INTO designacion (persona_id, dependencia_id, puesto_id, articulo_id, fecha) VALUES(%s, %s, %s, %s, %s)" }

    db_queries = {'puesto'        : u"SELECT id FROM puesto WHERE nombre = %s",
                  'dependencia'   : u"SELECT id FROM dependencia WHERE nombre = %s",
                  'persona'       : u"SELECT id FROM persona_2 WHERE codigo_tipo = %s and codigo_numero = %s"}

    correctos = 0
    sin_datos = 0
    for aviso_path in avisos_path:
        if aviso_path.find('decreto') >= 0:
            with open(aviso_path, 'r') as aviso_file:
                aviso_str = aviso_file.read()
                designaciones = DecretoParser.get_designaciones(aviso_str)
                if designaciones and len(designaciones) > 0:

                    # Fecha de la designacion
                    designacion_fecha = os.path.basename(os.path.dirname(aviso_path)) 

                    for designacion in designaciones:
                        # Puesto
                        puesto = "Sin puesto"
                        if len(designacion.puestos) > 0:
                            puesto =  designacion.puestos[0]

                        cursor.execute(db_queries['puesto'], puesto.upper())
                        puesto_db = cursor.fetchone()
                        if puesto_db:
                            puesto_id = puesto_db[0]
                        else:
                            cursor.execute(db_inserts['puesto'], puesto.upper())
                            puesto_id = cursor.lastrowid

                        # Dependencia
                        dependencia =  designacion.dependencia
                        if not dependencia:
                            dependencia = "Sin dependencia"

                        cursor.execute(db_queries['dependencia'], dependencia.upper())
                        dependencia_db = cursor.fetchone()
                        if dependencia_db:
                            dependencia_id = dependencia_db[0]
                        else:
                            cursor.execute(db_inserts['dependencia'], dependencia.upper())
                            dependencia_id = cursor.lastrowid

                        # Persona
                        persona = designacion.persona
                        if persona.codigo_tipo and persona.codigo_numero:
                            cursor.execute(db_queries['persona'], (persona.codigo_tipo, persona.codigo_numero))
                            persona_db = cursor.fetchone()
                            if not persona_db:
                                cursor.execute(db_inserts['persona'],(persona.nombre.upper().encode('utf8'), persona.codigo_tipo, persona.codigo_numero))
                                persona_id = cursor.lastrowid
                            else:
                                persona_id = persona_db[0]

                            cursor.execute(db_inserts['articulo'], designacion.articulo_texto)
                            articulo_id = cursor.lastrowid   
                            try:
                                cursor.execute(db_inserts['designacion'],(persona_id, dependencia_id, puesto_id, articulo_id, designacion_fecha))
                                correctos += 1
                                print "+"
                            except:
                                import pdb; pdb.set_trace()
                                sin_datos += 1
                        else:
                            sin_datos += 1
                            print "."

    print "correctos:", correctos, "sin_datos:", sin_datos

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print >>sys.stderr, 'usage: download_pdf.py path'
        sys.exit(2)

    #conn = MySQLdb.connect(host = 'localhost', 
    #                        db = 'boletin_oficial',
    #                        user = 'banquito', 
    #                        passwd = 'banquito', 
    #                        charset = "utf8", 
    #                        use_unicode = True)

    conn = MySQLdb.connect(host = 'clodo.dyndns.info', 
                            db = 'boletin_oficial',
                            user = 'clodo', 
                            passwd = 'cjbidau', 
                            charset = "utf8", 
                            use_unicode = True)

    cursor = conn.cursor()
    error = 0
    dates_path = [sys.argv[1] + x for x in os.listdir(sys.argv[1])]
    for date_path in dates_path:
        avisos_path = [date_path  + '/'+ x for x in os.listdir(date_path)]
        popular_primera_seccion(avisos_path, cursor)
        conn.commit()

    cursor.close()
    conn.close()
