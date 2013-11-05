# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import logging
from models import Persona, Decreto, Designacion

# Siento que esto esta mal
TITULOS = (u"D[a]?\.", u"Mayor", u"Abogad[ao]+", u"Dr[a\.]\.?", u"señor[a]?", 
           u"don", u"doña", "doctor[a]?",
           u"profesor[a]?",u"agente", "licenciad[ao]",
           u"contador[oa\s]+públic[oa][\s]+nacional", 
           u"sr[a]?\.", u"cdora\.", u"contador[ao]", )


logging_msg = """ ------------- %s -------------
%s \n"""

logging.basicConfig(format="%(message)s", filename='error.log', 
                    filemode = "w", level = logging.ERROR)

class BoletinParser():
# TODO: abstraer la logica en un metodo de decretos y articulos
    @classmethod
    def get_decretos(cls, boletin_str):
        decreto_inicio_re = re.compile(u'^#I(\d)+I#$', re.UNICODE)
        decreto_fin_re = re.compile(u'#F(\d)+F#', re.UNICODE)
        decretos = []
        en_decreto = False
        decreto = ""
        for line in boletin_str.split('\n'):
            if decreto_inicio_re.match(line):
                en_decreto = True
            elif decreto_fin_re.match(line):
                en_decreto = False
                decretos.append(decreto)
                decreto = ""
            elif en_decreto:
                decreto += line + "\n"

        if en_decreto:
           decretos.append(decreto)

        return decretos

    @classmethod
    def get_articulos(cls, decreto_str):
        articulo_inicio_str = u'(art\.|articulo|art\xc3\xadculo)+\s+\d\xc2\xba'
        articulo_inicio_re = re.compile(articulo_inicio_str, re.U | re.I)
        articulos = []
        en_articulo = False
        articulo = ""
        for line in decreto_str.split('\n'):
            if articulo_inicio_re.match(line):
                if en_articulo:
                    articulos.append(articulo)
                    articulo = ""
                else:
                    en_articulo = True

            if en_articulo:
                articulo += line + "\n"

        if en_articulo:
           articulos.append(articulo)

        return articulos

class DecretoParser():
    @classmethod
    def get_designaciones(cls, decreto_xml_str = None, decreto_str = None):
        if decreto_xml_str:
            return cls.__get_designaciones_xml(decreto_xml_str)
        else:
            return cls.__get_designaciones_str(decreto_str)

    @classmethod
    def __get_designaciones_xml(cls, decreto_xml_str):
        decreto_xml = BeautifulSoup(decreto_xml_str)

        if not ((decreto_xml.find('anexo') and decreto_xml.find('table'))):
            articulos = [Articulo(x) for x in decreto_xml.find_all('articulo')] 
            designaciones = [x.designacion for x in articulos if x.es_una_designacion]
        else:
            anexo = Anexo(decreto_xml.find('anexo'))
            designaciones = anexo.designaciones

        return designaciones

    @classmethod
    def __get_designaciones_str(cls, decreto_str):
        pass


# TODO: Hay que pasar articulo y anexo a una clase llamada DesignacionParser
class Articulo():
    def __init__(self, articulo_xml):
        self.texto = articulo_xml.text.replace('\n',' ').strip()  
        self.es_una_designacion = False

        designacion_match = re.search(u"des[ií]+gn", self.texto, re.IGNORECASE | re.UNICODE)
        if designacion_match:
            pos = designacion_match.start()
            self.es_una_designacion = True
            # Buscamos a la persona
            persona_nombre = PersonaParser.get_nombre_desde_articulo(self.texto)
            if not persona_nombre:
                logging.error(logging_msg, "No se encontro a la PERSONA", articulo_xml)

            persona_codigo = PersonaParser.get_codigo_desde_articulo(self.texto)
            if not persona_codigo[0]:
                logging.error(logging_msg, "No se encontro el CODIGO TIPO", articulo_xml)
            if not persona_codigo[1]:
                logging.error(logging_msg, "No se encontro el CODIGO NUMERO", articulo_xml)

            persona = Persona(persona_nombre, persona_codigo[0], persona_codigo[1])

            # Buscamos los puestos y la dependencia
            puestos = PuestoParser.get_puestos(self.texto)
            if len(puestos) == 0:
                logging.error(logging_msg, "No se encontraron PUESTOS", articulo_xml)
            dependencia = PuestoParser.get_dependencia(self.texto)
            if not dependencia:
                logging.error(logging_msg, "No se encontro la DEPENDENCIA", articulo_xml)

            self.designacion = Designacion(persona, puestos, dependencia, self.texto)


# TODO: Ver una manera de tratar las diferentes tablas
class Anexo():
    def __init__(self, anexo_xml):
        self.texto = anexo_xml.text.replace('\n',' ').strip()  
        self.columnas = [x for x in anexo_xml.find_all('td') if x.get_text()]
        self.designaciones = []
        # Arreglar de alguna manera esta negrada
        # Por el momento identificamos 4 tipos de tablas diferentes, hay muchas mas
        # CAMBIAR ESTO, NO SIRVE PARA NADA
        tabla_tipo = 0
        for i in range(len(self.columnas)):
            #B 0 - FE II
            columna = self.columnas[i].text
            columna_sig = self.columnas[i].text
            if re.search(u'^[A-Z] \d - [A-Z][A-Z] [A-Z][A-Z]$', columna) and \
                (tabla_tipo == 0 or tabla_tipo == 1):

                persona_nombre = self.columnas[i+1].text
                persona_codigo = PersonaParser.get_codigo(self.columnas[i+2].text)
                persona = Persona(persona_nombre, persona_codigo[0], persona_codigo[1])
                puestos = [self.columnas[i-1].text.upper()]
                dependencia = self.columnas[i-2].text.upper()

                self.designaciones.append(Designacion(persona, puestos, dependencia, self.texto))

                if tabla_tipo == 0:
                    tabla_tipo = 1
            elif columna == u"DNI" and \
                (tabla_tipo == 0 or tabla_tipo == 2):

                persona_nombre = u"{0} {1}".format(self.columnas[i-1].text, self.columnas[i-2].text)
                codigo_texto = u"DNI {0}".format(self.columnas[i+1].text)
                persona_codigo = PersonaParser.get_codigo(codigo_texto)
                persona = Persona(persona_nombre, persona_codigo[0], persona_codigo[1])
                puestos = [self.columnas[i+3].text.upper()]
                dependencia = self.columnas[i+2].text.upper()

                self.designaciones.append(Designacion(persona, puestos, dependencia, self.texto))

                if tabla_tipo == 0:
                    tabla_tipo = 2

            elif re.search(u'^[A-Z]$', columna) and  \
                (tabla_tipo == 0 or tabla_tipo == 3):

                persona_nombre = self.columnas[i-2].text
                codigo_texto = self.columnas[i-1].text
                if re.search(u"\d\d\d\.\d\d\d", persona_nombre):
                    codigo_texto, persona_nombre = persona_nombre, codigo_texto

                persona_codigo = PersonaParser.get_codigo(codigo_texto)
                persona = Persona(persona_nombre, persona_codigo[0], persona_codigo[1])
                try:
                    puestos = [self.columnas[i+2].text.upper()]
                except IndexError:
                    puestos = []

                # No se encuentra la dependencia
                self.designaciones.append(Designacion(persona, puestos, None, self.texto))

                if tabla_tipo == 0:
                    tabla_tipo = 3

            elif re.search(u'^[A-Z]-\d$', columna) and  \
                (tabla_tipo == 0 or tabla_tipo == 4):

                persona_nombre = self.columnas[i-2].text
                codigo_texto = self.columnas[i-1].text
                if re.search(u"\d\d\d\.\d\d\d", persona_nombre):
                    codigo_texto, persona_nombre = persona_nombre, codigo_texto

                persona_codigo = PersonaParser.get_codigo(codigo_texto)
                persona = Persona(persona_nombre, persona_codigo[0], persona_codigo[1])
                try:
                    puestos = [self.columnas[i+1].text.upper()]
                except IndexError:
                    puestos = []
                # No se encuentra la dependencia
                self.designaciones.append(Designacion(persona, puestos, None, self.texto))

                if tabla_tipo == 0:
                    tabla_tipo = 4

class PersonaParser():
    CODIGO_STR_RE = u"([LEDNIM.]+)[MNnº°:\s]+([\d.]+)"

    @classmethod
    def get_nombre_desde_articulo(cls, texto):
        codigo_str_re = u"\({0}\)".format(cls.CODIGO_STR_RE)
        codigo_match = re.search(codigo_str_re, texto, re.UNICODE)
        if codigo_match:
            texto = texto[:codigo_match.start()]

        persona_str_re = \
                u"""\s+({0})   # Titulo
                ([.\s\w]*)        # Persona""".format("|".join(TITULOS))

        persona_re = \
            re.compile(persona_str_re, re.X | re.IGNORECASE | re.UNICODE)

        persona_match = persona_re.search(texto)
        nombre = ""
        if persona_match:
            nombre = persona_match.groups()[1].strip()
            # Le agregamos un espacio asi coincide con el patron de busqueda
            tiene_dos_titulos = persona_re.search(" " + nombre)
            if tiene_dos_titulos:
                nombre = tiene_dos_titulos.groups()[1].strip()

        return nombre

    @classmethod
    def get_codigo_desde_articulo(cls, texto):
        codigo_str_re = u"\({0}\)".format(cls.CODIGO_STR_RE)
        return cls.get_codigo(texto, codigo_str_re) 

    @classmethod
    def get_codigo(cls, texto, codigo_str_re = None):
        if not codigo_str_re:
            codigo_str_re = cls.CODIGO_STR_RE

        codigo_match = re.search(codigo_str_re, texto, re.UNICODE)
        if codigo_match:
            tipo = codigo_match.groups()[0].replace('.','').upper()
            numero = codigo_match.groups()[1].replace('.','')
        else:
            tipo = None
            if re.search(u"\d\d\d\.\d\d\d", texto):
                numero = texto.replace('.','')
            else:
                numero = None

        return (tipo, numero)

class PuestoParser():
    # No se usa la expresino de abajo, porque no funcionaba,
    # no encuentra el "del" o "de la" a veces, pero como esta abajo si.
    #DEPENDENCIA_RE = re.compile(u"(del|de la)\s*[A-Z][A-Z]+")
    PUESTO_KEYWORDS = (u"como",u"en el cargo de", u"en la función de",
                              u"cumplir funciones de", )
    
    # Tratamos las keywords de SINEP diferente, porque generalmente
    # no dice que puesto se designa sino su Nivel y Grado
    # pero a veces lo dice y ahi es cuando se producen contradicciones
    # dandole mas prioridad al Nivel y Grado que al puesto otorgado
    SINEP_KEYWORDS = (u"en un cargo (vacante)?")
    
    @classmethod
    def get_puestos(cls, texto):
        """ Obtenemos los puestos devolviendo una lista de puestos 
        """
        # Buscamos las keywords del antes del puesto
        puesto_token_match_start = \
                re.search(u"({0})".format("|".join(cls.PUESTO_KEYWORDS)), texto, re.UNICODE)

        puestos = []
        if puesto_token_match_start:
            # Buscamos las keywords antes del comienzo de la Dependencia
            texto = texto[puesto_token_match_start.end():]

            puesto_token_match_end = re.search(u"(del|de la)", texto, re.UNICODE)
            if puesto_token_match_end:
                texto = texto[:puesto_token_match_end.start()]

            # Puede tener multiples puestos y estar en minisculas o en mayusculas
            for puesto_texto in texto.split('y'):
                puesto_match = re.findall(u"""
                            \s*  
                            ([A-Z][a-záéíóú\d]+  # Director Titular
                            |[A-ZÁÉÍÓÚ\d]+)      # DIRECTOR TITULAR
                            \s*""", puesto_texto, re.X | re.UNICODE)
                # Unimos a las palabras del puesto, (Director, Titular) -> Director Titular
                puesto = " ".join([x.strip().upper() for x in puesto_match])
                puestos.append(puesto)
        # Si no las encontramos, nos fijamos en las keywords de SINEP
        else:
            puesto_match = re.search(u"(Nivel\s+[A-Z])[\s,-]+(Grado\s+\d)", texto, re.UNICODE)
            if puesto_match:
                puesto = " ".join([x.strip().upper() for x in puesto_match.groups()])
                puestos.append(puesto)

        return puestos

    @classmethod
    def get_dependencia(cls, texto):
        """ Obtenemos la dependencia
        """
        # Primero vamos a acortar desde-hasta buscamos el nombre
        # de la dependencia
        dependencia_match_start = re.search(u"(del|de la)\s*[A-Z][A-Z]+", texto, re.UNICODE)
        if dependencia_match_start: 
            texto_begin = dependencia_match_start.start() + len(dependencia_match_start.groups()[0])
            texto = texto[texto_begin:]

        dependencia_token_match_end = re.search(u"[^A-Z\s]+", texto, re.UNICODE)
        if dependencia_token_match_end:
            texto = texto[:dependencia_token_match_end.start()]

        dependencia_match = re.findall(u"\s*[A-ZÁÉÍÓÚ]+\s*", texto, re.X | re.UNICODE)
        dependencia = " ".join([x.strip().upper() for x in dependencia_match])

        return dependencia

