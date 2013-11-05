# -*- coding: utf-8 -*-
class Boletin():
    def __init__(self, decretos):
        self.decretos = decretos

class Decreto():
    def __init__(self, designaciones, decreto_str = None):
        self.designaciones = designaciones

class Designacion():
    def __init__(self, persona, puestos, dependencia = None, articulo_texto = None, fecha = None):
        self.persona = persona
        self.puestos = puestos
        self.dependencia = dependencia
        self.articulo_texto = articulo_texto 
        self.fecha = fecha

class Persona():
    def __init__(self, nombre, codigo_tipo, codigo_numero):
        self.nombre = nombre
        self.codigo_tipo = codigo_tipo
        self.codigo_numero = codigo_numero
