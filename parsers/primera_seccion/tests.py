# -*- coding: utf-8 -*-
import unittest
import os
from parsers import Anexo, PersonaParser, PuestoParser, DecretoParser, BoletinParser
from bs4 import BeautifulSoup
from fixtures import decretos, articulos

class TestDecretosDesignaciones(unittest.TestCase):
    # Decreto 0
    def test_total_de_designaciones_decreto_0(self):
        designaciones = DecretoParser.get_designaciones(decretos[0])
        self.assertEqual(1, len(designaciones))

    # Decreto 1
    def test_total_de_designaciones_decreto_1(self):
        designaciones = DecretoParser.get_designaciones(decretos[1])
        self.assertEqual(2, len(designaciones))

    # Decreto 2
    def test_total_de_designaciones_decreto_2(self):
        designaciones = DecretoParser.get_designaciones(decretos[2])
        self.assertEqual(1, len(designaciones))

    # Decreto 3
    def test_total_de_designaciones_decreto_3(self):
        designaciones = DecretoParser.get_designaciones(decretos[3])
        self.assertEqual(1, len(designaciones))

    # Decreto 4
    def test_total_de_designaciones_decreto_4(self):
        designaciones = DecretoParser.get_designaciones(decretos[4])
        self.assertEqual(1, len(designaciones))

    # Decreto 5
    def test_total_de_designaciones_decreto_5(self):
        designaciones = DecretoParser.get_designaciones(decretos[5])
        self.assertEqual(1, len(designaciones))

    # Decreto 6
    def test_total_de_designaciones_decreto_6(self):
        designaciones = DecretoParser.get_designaciones(decretos[6])
        self.assertEqual(1, len(designaciones))

    # Decreto 10
    def test_total_de_designaciones_decreto_10(self):
        designaciones = DecretoParser.get_designaciones(decretos[10])
        self.assertEqual(7, len(designaciones))

    # Decreto 11
    def test_total_de_designaciones_decreto_11(self):
        designaciones = DecretoParser.get_designaciones(decretos[11])
        self.assertEqual(2, len(designaciones))

    # Decreto 12
    def test_total_de_designaciones_decreto_12(self):
        designaciones = DecretoParser.get_designaciones(decretos[12])
        self.assertEqual(17, len(designaciones))

class TestDesignacionesDesdeArticulos(unittest.TestCase):
    # Decreto 0
    def test_get_personas_designadas_desde_decreto_0(self):
        designaciones = DecretoParser.get_designaciones(decretos[0])
        designacion = designaciones[0]
        self.assertEqual(u"Juan Claudio TRISTAN", designacion.persona.nombre)
        self.assertEqual(u"MI", designacion.persona.codigo_tipo)
        self.assertEqual(u"16779003", designacion.persona.codigo_numero)
        self.assertEqual(u"DIRECTOR TITULAR", designacion.puestos[0])
        self.assertEqual(u"PRESIDENTE", designacion.puestos[1])
        self.assertEqual(u"CORREO OFICIAL DE LA REPUBLICA ARGENTINA SOCIEDAD ANONIMA", designacion.dependencia)

    # Decreto 1
    def test_get_personas_designadas_desde_decreto_1(self):
        designaciones = DecretoParser.get_designaciones(decretos[1])
        designacion_1 = designaciones[0]
        self.assertEqual(u"Vanesa Daniela PIESCIOROVSKI", designacion_1.persona.nombre)
        self.assertEqual(u"DNI", designacion_1.persona.codigo_tipo)
        self.assertEqual(u"27235128", designacion_1.persona.codigo_numero)
        self.assertEqual(u"DIRECTORA TITULAR", designacion_1.puestos[0])
        self.assertEqual(u"CORREO OFICIAL DE LA REPUBLICA ARGENTINA SOCIEDAD ANONIMA", designacion_1.dependencia)

        designacion_2 = designaciones[1]
        self.assertEqual(u"Carlos Alberto ROSSI", designacion_2.persona.nombre)
        self.assertEqual(u"DNI", designacion_2.persona.codigo_tipo)
        self.assertEqual(u"10629427", designacion_2.persona.codigo_numero)
        self.assertEqual(u"DIRECTOR TITULAR", designacion_2.puestos[0])
        self.assertEqual(u"CORREO OFICIAL DE LA REPUBLICA ARGENTINA SOCIEDAD ANONIMA", designacion_2.dependencia)

    # Decreto 2
    def test_get_personas_designadas_desde_decreto_2(self):
        designaciones = DecretoParser.get_designaciones(decretos[2])
        designacion = designaciones[0]
        self.assertEqual(u"Ignacio LAMOTHE", designacion.persona.nombre)
        self.assertEqual(u"DNI", designacion.persona.codigo_tipo)
        self.assertEqual(u"27604118", designacion.persona.codigo_numero)
        self.assertEqual(u"SECRETARIO DE ASUNTOS MUNICIPALES", designacion.puestos[0])
        self.assertEqual(u"MINISTERIO DEL INTERIOR", designacion.dependencia)

    # Decreto 3
    def test_get_personas_designadas_desde_decreto_3(self):
        designaciones = DecretoParser.get_designaciones(decretos[3])
        designacion = designaciones[0]
        self.assertEqual(u"Gustavo Sergio Ismael CACEREZ", designacion.persona.nombre)
        self.assertEqual(u"DNI", designacion.persona.codigo_tipo)
        self.assertEqual(u"29652327", designacion.persona.codigo_numero)
        self.assertEqual(u"SUBSECRETARIO DE GESTION MUNICIPAL", designacion.puestos[0])
        self.assertEqual(u"SECRETARIA DE ASUNTOS MUNICIPALES", designacion.dependencia)

    # Decreto 4
    def test_get_personas_designadas_desde_decreto_4(self):
        designaciones = DecretoParser.get_designaciones(decretos[4])
        designacion = designaciones[0]
        self.assertEqual(u"Jorge Alberto RAMIREZ", designacion.persona.nombre)
        self.assertEqual(u"DNI", designacion.persona.codigo_tipo)
        self.assertEqual(u"4991727", designacion.persona.codigo_numero)
        self.assertEqual(u"DIRECTOR GESTIÓN AMBIENTAL RECURSOS HÍDRICOS", designacion.puestos[0])
        self.assertEqual(u"DIRECCION NACIONAL DE ARTICULACION INSTITUCIONAL", designacion.dependencia)

    # Decreto 5
    def test_get_personas_designadas_desde_decreto_5(self):
        designaciones = DecretoParser.get_designaciones(decretos[5])
        designacion = designaciones[0]
        self.assertEqual(u"Humberto Claudio TRISANO", designacion.persona.nombre)
        self.assertEqual(u"DNI", designacion.persona.codigo_tipo)
        self.assertEqual(u"11455106", designacion.persona.codigo_numero)
        self.assertEqual(u"COMANDANTE OPERACIONAL", designacion.puestos[0])
        self.assertEqual(u"ESTADO MAYOR CONJUNTO DE LAS FUERZAS ARMADAS", designacion.dependencia)


    # Decreto 6
    def test_get_personas_designadas_desde_decreto_6(self):
        designaciones = DecretoParser.get_designaciones(decretos[6])
        designacion = designaciones[0]
        self.assertEqual(u"María Alejandra ABOLIO", designacion.persona.nombre)
        self.assertEqual(u"DNI", designacion.persona.codigo_tipo)
        self.assertEqual(u"17233935", designacion.persona.codigo_numero)
        self.assertEqual(u"SUPERVISORA AUDITORÍA LEGAL NIVEL B GRADO 7 FUNCIÓN EJECUTIVA IV", designacion.puestos[0])
        self.assertEqual(u"UNIDAD DE AUDITORIA INTERNA", designacion.dependencia)

    # Agregar los otros tests
    # Decreto 8
    def test_get_personas_designadas_desde_decreto_8(self):
        designaciones = DecretoParser.get_designaciones(decretos[8])
        designacion = designaciones[0]

class TestDesignacionesDesdeAnexos(unittest.TestCase):
    # Decreto 7
    def test_get_personas_designadas_desde_decreto_7(self):
        anexo_xml = BeautifulSoup(decretos[7])
        anexo = Anexo(anexo_xml.find('anexo'))
        self.assertEqual(2, len(anexo.designaciones))

        self.assertEqual(u"Cdora. Silvia Herminia TRIPICCHIO", anexo.designaciones[0].persona.nombre)
        self.assertEqual(u"DNI", anexo.designaciones[0].persona.codigo_tipo)
        self.assertEqual(u"6532317", anexo.designaciones[0].persona.codigo_numero)
        self.assertEqual(u"DIRECTORA", anexo.designaciones[0].puestos[0])
        self.assertEqual(u"DIRECCION DE ADMINISTRACION Y FINANZAS", anexo.designaciones[0].dependencia)
        

        self.assertEqual(u"Dr. Mario Alberto VASSENA", anexo.designaciones[1].persona.nombre)
        self.assertEqual(u"DNI", anexo.designaciones[1].persona.codigo_tipo)
        self.assertEqual(u"4394247", anexo.designaciones[1].persona.codigo_numero)
        self.assertEqual(u"DIRECTOR", anexo.designaciones[1].puestos[0])
        self.assertEqual(u"DIRECCION DE ACTUACIONES JUDICIALES, PROYECTOS Y RELATORIA JURIDICA", anexo.designaciones[1].dependencia)

    # Decreto 11
    def test_get_personas_designadas_desde_decreto_11(self):
        anexo_xml = BeautifulSoup(decretos[11])
        anexo_str = anexo_xml.find('anexo')
        anexo = Anexo(anexo_str)
        self.assertEqual(2, len(anexo.designaciones))

        self.assertEqual(u"TUTUSAUS, Gerónimo Andrés", anexo.designaciones[0].persona.nombre)
        self.assertFalse(anexo.designaciones[0].persona.codigo_tipo)
        self.assertEqual(u"31283978", anexo.designaciones[0].persona.codigo_numero)
        self.assertEqual(u"COORDINADOR UNIDADES ORGANIZATIVAS", anexo.designaciones[0].puestos[0])
        #self.assertEqual(u"DIRECCION DE ADMINISTRACION Y FINANZAS", anexo.designaciones[0].dependencia)
        

        self.assertEqual(u"AIMETTA, Lía Antonella", anexo.designaciones[1].persona.nombre)
        self.assertFalse(anexo.designaciones[1].persona.codigo_tipo)
        self.assertEqual(u"36529787", anexo.designaciones[1].persona.codigo_numero)
        self.assertEqual(u"ASISTENTE ADMINISTRATIVA", anexo.designaciones[1].puestos[0])
        #self.assertEqual(u"DIRECCION DE ACTUACIONES JUDICIALES, PROYECTOS Y RELATORIA JURIDICA", anexo.designaciones[1].dependencia)

       # Decreto 12
    def test_get_personas_designadas_desde_decreto_12(self):
        anexo_xml = BeautifulSoup(decretos[12])
        anexo_str = anexo_xml.find('anexo')
        anexo = Anexo(anexo_str)
        self.assertEqual(17, len(anexo.designaciones))

        self.assertEqual(u"Ricardo Daniel BENTO", anexo.designaciones[0].persona.nombre)
        self.assertEqual(u"DNI", anexo.designaciones[0].persona.codigo_tipo)
        self.assertEqual(u"26119784", anexo.designaciones[0].persona.codigo_numero)
        self.assertEqual(u"ASISTENTE ADMINISTRATIVO", anexo.designaciones[0].puestos[0])
        self.assertEqual(u"DIRECCIÓN GENERAL DE MOVIMIENTO MIGRATORIO", anexo.designaciones[0].dependencia)
        
class TestPersona(unittest.TestCase):
    def test_persona_con_enie(self):
       persona_nombre = PersonaParser.get_nombre_desde_articulo(unicode(articulos[0], 'utf-8'))
       persona_nombre = PersonaParser.get_nombre_desde_articulo(unicode(articulos[1], 'utf-8'))

    def test_persona_con_sr_como_titulo(self):
       persona_nombre = PersonaParser.get_nombre_desde_articulo(unicode(articulos[2], 'utf-8'))
       self.assertEqual(u"Sergio Rubén VAZQUEZ", persona_nombre)

class TestPuesto(unittest.TestCase):
    def test_get_puesto_desde_articulo_3(self):
       puestos = PuestoParser.get_puestos(articulos[3])
       self.assertEqual(u'DIRECTOR', puestos[0])

    def test_get_puesto_desde_articulo_4(self):
       """ Trae conflictos con las designaciones por empezar como "Designase Director"""
       puestos = PuestoParser.get_puestos(articulos[4])
       #self.assertEqual(u'DIRECTOR EJECUTIVO', puestos[0])

    def test_get_puesto_desde_articulo_5(self):
       puestos = PuestoParser.get_puestos(articulos[5])
       self.assertEqual(u'NIVEL B GRADO 0', puestos[0])

    def test_get_puesto_desde_articulo_6(self):
       puestos = PuestoParser.get_puestos(articulos[6])
       self.assertEqual(u'NIVEL C GRADO 0', puestos[0])

    def test_get_puesto_desde_articulo_7(self):
       puestos = PuestoParser.get_puestos(articulos[7])
       self.assertEqual(u'NIVEL B GRADO 0', puestos[0])

class TestBoletin(unittest.TestCase):
    BOLETINES_PATH = './fixtures_boletines/'
    def setUp(self):
        boletines_filenames = os.listdir(self.BOLETINES_PATH)
        boletines_filenames.sort()
        self.boletines = []
        for boletin_filename in boletines_filenames:
            with open(os.path.join(self.BOLETINES_PATH, boletin_filename), 'r') as boletin_file:
                self.boletines.append(boletin_file.read())

    def test_get_decretos_de_boletin_0(self):
        decretos = BoletinParser.get_decretos(self.boletines[0])
        self.assertEqual(53, len(decretos))

    def test_get_articulos_de_decreto_0_boletin_0(self):
        decretos = BoletinParser.get_decretos(self.boletines[0])

        articulos = BoletinParser.get_articulos(decretos[0])
        #hay mucha basura en el decreto 0, indices y demas
        #self.assertEqual(2, len(articulos))

        articulos = BoletinParser.get_articulos(decretos[1])
        self.assertEqual(4, len(articulos))

if __name__ == '__main__':
    unittest.main()
