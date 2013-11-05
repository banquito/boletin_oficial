from models import Decreto
from datetime import datetime
import os
import traceback
import sys

boletines_path = "./boletines/xmls/"
def parsear_decreto():
    pass

decretos = 0
decretos_con_error = 0
decretos_sin_designacion = 0
decretos_anexos = 0
decretos_articulos = 0
total_decretos = 0
total_puestos = 0
total_designaciones = 0
if __name__ == '__main__':
    parser_started_at = datetime.now()

    for boletin_name in os.listdir(boletines_path):
        boletin_path = os.path.join(boletines_path, boletin_name)
        for aviso_name in os.listdir(boletin_path):
            if aviso_name.find('decreto') >= 0:
                total_decretos += 1
                aviso_path = os.path.join(boletin_path, aviso_name)
                with open(aviso_path, 'r') as aviso_file:
                    aviso_str = aviso_file.read()
                    try:
                        decreto = Decreto(aviso_str)
                        if decreto.designaciones and len(decreto.designaciones) > 0:
                            decretos += 1
                            for designacion in decreto.designaciones:
                                total_designaciones += 1
                                puesto = "Sin puesto"
                                if len(designacion.puestos) > 0:
                                    total_puestos += 1
                                    puesto =  designacion.puestos[0]

                                persona = designacion.persona
                                codigo = "Sin codigo"
                                if persona.codigo_tipo:
                                    codigo = "{0} {1}".format(persona.codigo_tipo.encode('utf-8').upper(), persona.codigo_numero)
                                print "{0},{1},{2},{3}".format(codigo, persona.nombre.encode('utf-8').upper(), puesto.encode('utf-8'), designacion.dependencia.encode('utf-8'))
                                

                        else:
                            decretos_sin_designacion += 1

                    except:
                        decretos_con_error += 1
                        #traceback.print_exc(file=sys.stdout)



    print "Decretos con designacion:", decretos, "Sin Designacion:", decretos_sin_designacion
    print "Designaciones de Articulos", decretos_articulos
    print "Designaciones de Anexos", decretos_anexos
    print "Designaciones con puestos", total_puestos
    print "Total:", total_decretos, "Con error:", decretos_con_error

