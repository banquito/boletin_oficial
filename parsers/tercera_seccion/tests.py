# -*- coding: utf-8 -*-
import unittest
from models import Adjudicacion, Boletin, PruebaDB
import fixtures

class TestAdjudicaciones(unittest.TestCase):
    def test_when_empty_return_texto_empty(self):
        adjudicacion = Adjudicacion()
        self.assertFalse(bool(adjudicacion.get_texto()))
    
    def test_when_nestor_return_texto_nestor(self):
        adjudicacion = Adjudicacion("Nestor")
        self.assertEqual(adjudicacion.get_texto(), "Nestor")

    def test_when_adjudicacion_0_return_entidad_publica(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[0])
        self.assertEqual(adjudicacion.get_entidad_publica(), 
            "FUERZA AEREA ARGENTINA ESTADO MAYOR GENERAL DE LA FUERZA AEREA INSTITUTO DE FORMACION EZEIZA")

    def test_when_adjudicacion_0_return_proveedor(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[0])
        proveedores = adjudicacion.get_proveedores()
        self.assertTrue("METEO S.A. " in proveedores)

    def test_when_adjudicacion_0_return_proveedor2(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[8])
        proveedores = adjudicacion.get_proveedores()
        precios = adjudicacion.get_precios()

        self.assertTrue("LA LEY S.A." in proveedores)
        self.assertEqual("LA LEY S.A.", proveedores[0])
        self.assertEqual(len(proveedores), len(precios))

    def test_when_adjudicacion_0_return_proveedor3(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[9])
        proveedores = adjudicacion.get_proveedores()
        precios = adjudicacion.get_precios()
        self.assertEqual(len(proveedores), len(precios))
    
    def test_when_adjudicacion_0_return_precios(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[0])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "$" and precios[0]["valor"] == 87900)

    def test_when_adjudicacion_1_return_entidad_publica(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[1])
        self.assertEqual(adjudicacion.get_entidad_publica(), 
            "FUERZA AEREA ARGENTINA DIRECCION GENERAL DE INTENDENCIA DIRECCION DE CONTRATACIONES")

    def test_when_adjudicacion_1_return_proveedor(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[1])
        self.assertTrue("CAE USA INC." in adjudicacion.get_proveedores());

    def test_when_adjudicacion_1_return_objeto(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[1])
        self.assertEqual(adjudicacion.get_objeto(), "Cursos de Mantenimiento de Motores T-56.")

    def test_when_adjudicacion_1_return_precios(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[1])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "U$S" and precios[0]["valor"] == 74076)

    def test_when_adjudicacion_2_return_entidad_publica(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[2])
        self.assertEqual(adjudicacion.get_entidad_publica(), 
            "EJERCITO ARGENTINO COLEGIO MILITAR DE LA NACION")

    def test_when_adjudicacion_2_return_objeto(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[2])
        self.assertEqual(adjudicacion.get_objeto(), "Adquisición de Combustibles y Lubricantes para el funcionamiento del Instituto en el 4to Trimestre 2011 y 1er Trimestre 2012.")

    def test_when_adjudicacion_2_return_proveedores(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[2])
        proveedores = adjudicacion.get_proveedores()
        self.assertTrue("LEONARDO MAZZEO" in proveedores)
        self.assertTrue("DISTRIBUIDORA SYNERGIA S.R.L." in proveedores)
        self.assertTrue("SUALIER SA" in proveedores)
        self.assertTrue("VIMI S.A." in proveedores)

    def test_when_adjudicacion_2_return_precios(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[2])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "$" and precios[0]["valor"] == 19906)
        self.assertTrue(precios[1]["moneda"] == "$" and precios[1]["valor"] == 19621.45)
        self.assertTrue(precios[2]["moneda"] == "$" and precios[2]["valor"] == 686950)
        self.assertTrue(precios[3]["moneda"] == "$" and precios[3]["valor"] == 34893.80)

    def test_when_adjudicacion_3_return_entidad_publica(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[3])
        self.assertEqual(adjudicacion.get_entidad_publica(), 
            "GENDARMERIA NACIONAL ARGENTINA")

    def test_when_adjudicacion_3_return_objeto(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[3])
        self.assertEqual(adjudicacion.get_objeto(), "Adquisición de Equipamiento Técnico para la Dirección de Policía Científica.")

    def test_when_adjudicacion_3_return_proveedores(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[3])
        proveedores = adjudicacion.get_proveedores()
        self.assertTrue("PROMETIN S.A." in proveedores)
        self.assertTrue("TECNOELECTRIC S.R.L." in proveedores)

    def test_when_adjudicacion_3_return_precios(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[3])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "$" and precios[0]["valor"] == 594)
        self.assertTrue(precios[1]["moneda"] == "$" and precios[1]["valor"] == 8577)

    def test_when_adjudicacion_4_return_entidad_publica(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[4])
        self.assertEqual(adjudicacion.get_entidad_publica(), 
            "ADMINISTRACION FEDERAL DE INGRESOS PUBLICOS DIRECCION REGIONAL ADUANERA MENDOZA")

    def test_when_adjudicacion_4_return_objeto(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[4])
        self.assertEqual(adjudicacion.get_objeto(), "Adquisición de Chombas de Piqué identificatorias.")

    def test_when_adjudicacion_4_return_proveedores(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[4])
        proveedores = adjudicacion.get_proveedores()    
        self.assertTrue("FEDERICO LOPEZ." in proveedores)

    def test_when_adjudicacion_4_return_precios(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[4])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "$" and precios[0]["valor"] == 44884.66)

    def test_when_adjudicacion_5_return_precios(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[5])
        precios = adjudicacion.get_precios()
        self.assertTrue(precios[0]["moneda"] == "$" and precios[0]["valor"] == 33900,00)

    def test_when_adjudicacion_6_return_objeto(self):
        adjudicacion = Adjudicacion(fixtures.adjudicaciones[6])
        self.assertEqual(adjudicacion.get_objeto(), "Mantenimiento Edilicio.")

#    def test_when_adjudicacion_7_return_objeto(self):
#        adjudicacion = Adjudicacion(fixtures.adjudicaciones[7])
#        self.assertEqual(adjudicacion.get_objeto(), "No tiene un objeto de adjudicacion")
        
class TestBoletinSeccion(unittest.TestCase):
    def test_when_boletin_has_seccion_adjudicaciones(self):
        boletin =  Boletin(fixtures.boletines[1]);
        self.assertTrue(boletin.tiene_seccion("Adjudicaciones"))

    def test_when_boletin_has_seccion_adjudicaciones2(self):
        boletin =  Boletin(fixtures.boletines[3]);
        self.assertTrue(boletin.tiene_seccion("Adjudicaciones"))

    def test_when_boletin_has_seccion_dictamenes_de_evaluacion(self):
        boletin =  Boletin(fixtures.boletines[1]);
        self.assertTrue(boletin.tiene_seccion("Dictámenes de Evaluación"))

    def test_when_boletin_has_seccion_servicios(self):
        boletin =  Boletin(fixtures.boletines[1]);
        self.assertTrue(boletin.tiene_seccion("Servicios Tres Palabras Audiovisuales"))

    def test_when_boletin_has_seccion_locaciones(self):
        boletin =  Boletin(fixtures.boletines[1]);
        self.assertTrue(boletin.tiene_seccion("Locaciones INMUEBLES \(LOC\)"))

    def test_when_boletin_doesnt_has_seccion_adjudicaciones(self):
        boletin =  Boletin(fixtures.boletines[1].replace("Adjudicaciones", "Preadjudicaciones"));
        self.assertFalse(boletin.tiene_seccion("Adjudicaciones"))

    def test_when_boletin_returns_from_seccion_adjudicaciones_copete(self):
        boletin = Boletin(fixtures.boletines[0]);
        self.assertEqual(boletin.get_desde_copete("Adjudicaciones"),
                         """
BANCO DE LA NACION ARGENTINA
AREA COMPRAS Y CONTRATACIONES""")

    def test_when_boletin_returns_from_seccion_adjudicaciones_copete2(self):
        boletin = Boletin(fixtures.boletines[4]);
        self.assertEqual(boletin.get_desde_copete("Adjudicaciones"),
                         """
EJERCITO ARGENTINO
COMANDO DE REMONTA
""")

    def test_when_boletin_returns_from_seccion_dictamenes_de_evaluacion_copete(self):
        boletin = Boletin(fixtures.boletines[1]);
        self.assertEqual(boletin.get_desde_copete("Dictámenes de Evaluación"),
                         """
BANCO DE LA NACION ARGENTINA
BANCO PIRULO
% 19 % #F4285852F#
Locaciones
INMUEBLES (LOC)
#I4286379I# % 19 % #N159046/11N#
AFIP""")

    def test_when_boletin_returns_nothing_from_seccion_adjudicaciones_copete(self):
        boletin = Boletin(fixtures.boletines[0].replace("Adjudicaciones", r"#I4284951I# % 23 % #N157178/11N#\nAdjudicaciones"))
        self.assertFalse(boletin.get_desde_copete("Adjudicaciones"))

    def test_when_boletin_return_next_copete(self):
        # Ver bien este donde se utiliza
        boletin = Boletin(fixtures.boletines[1]);
        self.assertEqual(boletin.get_proximo_copete(fixtures.boletines[1]),
                         """% 23 % #F4281795F#
Servicios Tres Palabras
Audiovisuales
#I4284951I# % 23 % #N157178/11N#""")

    def test_when_boletin_return_next_copete2(self):
        # Ver bien este donde se utiliza
        boletin = Boletin(fixtures.boletines[3]);
        self.assertEqual(boletin.get_proximo_copete(fixtures.boletines[5]),
                         """#F4080896F#
Servicios
COMUNICACIONES
#I4080375I#""")

    def test_when_boletin_return_seccion_adjudicacion(self):
        boletin = Boletin(fixtures.boletines[1]);
        self.assertEqual(boletin.get_seccion("Adjudicaciones"), """
BANCO DE LA NACION ARGENTINA
AREA COMPRAS Y CONTRATACIONES
% 23 % #F4285033F#
#I4285622I# % 23 % #N158007/11N#
BLOQUE1
% 23 % #F4285033F#
#I4285622I# % 23 % #N158007/11N#
BLOQUE2
% 23 % #F4285033F#
#I4285622I# % 23 % #N158007/11N#
BLOQUE3
""")

    def test_when_boletin_return_seccion_adjudicacion2(self):
        boletin = Boletin(fixtures.boletines[3]);
        self.assertEqual(boletin.get_seccion("Adjudicaciones"), """
EJERCITO ARGENTINO
COMANDO DE REMONTA 
Y VETERINARIA SUBASTA PUBLICA 
Nº 03/2010
Expediente Nº AF 10 – 219/5
DESIERTO DE OFERENTES
Objeto de la contratación: Subasta de 450 To-
neladas de Soja a granel, en el Establecimiento 
General Paz, Ruta Provincial 6 Km 153.5 – Or-
dóñez – Provincia de Córdoba.
Observaciones Generales:
Consulta del expediente: Comando de Remonta y 
Veterinaria - División Compras y Contrataciones, 2do 
Piso - Arévalo 3065 - Ciudad Autónóma de Buenos 
Aires - De lunes a viernes de 08:00 a 12:00 horas.
e. 15/03/2010 Nº 24766/10 v. 15/03/2010
""")

    def test_when_boletin_return_seccion_dictamenes_de_evaluacion(self):
        boletin = Boletin(fixtures.boletines[1]);
        self.assertEqual(boletin.get_seccion("Dictámenes de Evaluación"), """
BANCO DE LA NACION ARGENTINA
BANCO PIRULO
""")

    def test_when_boletin_return_seccion_servicios(self):
        boletin = Boletin(fixtures.boletines[1]);
        self.assertEqual(boletin.get_seccion("Servicios Tres Palabras Audiovisuales"), """
BLOQUE1
% 23 % #F4285033F#
#I4285622I# % 23 % #N158007/11N#
BLOQUE2
""")
    
    def test_when_boletin_returns_modulos_seccion_adjudicaciones(self):
        boletin = Boletin(fixtures.boletines[1])
        modulos = boletin.get_modulos_seccion("Adjudicaciones")        
        self.assertEqual(len(modulos), 4)
        self.assertTrue(modulos[0].find("BANCO DE LA NACION ARGENTINA"))
        self.assertTrue(modulos[2].find("BLOQUE2"))

    def test_when_boletin_returns_modulos_seccion_servicios(self):
        boletin = Boletin(fixtures.boletines[1])
        modulos = boletin.get_modulos_seccion("Servicios Tres Palabras Audiovisuales")
        self.assertEqual(len(modulos), 2)

    def test_when_boletin_returns_modulos_seccion_dictameneS(self):
        boletin = Boletin(fixtures.boletines[1])
        modulos = boletin.get_modulos_seccion("Dictámenes de Evaluación")
        self.assertEqual(len(modulos), 1)

if __name__ == '__main__':
    unittest.main()
