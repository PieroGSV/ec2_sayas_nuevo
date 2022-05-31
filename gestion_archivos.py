# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:50:18 2022

@author: PIERO
"""

import os
# ALUMNO SAYAS DE LA VEGA PIERO GABRIEL
def crear_archivo(nombre,contenido):
    archivo= open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()

# ALUMNO SAYAS DE LA VEGA PIERO GABRIEL
def eliminar_archivo(nombre):
    os.remove(nombre)
    
# ALUMNO SAYAS DE LA VEGA PIERO GABRIEL
def agregar_contenido_archivo(nombre,contenido):
    archivo=open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()
    
# ALUMNO SAYAS DE LA VEGA PIERO GABRIEL
def leer_achivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido= archivo.read()
    return contenido
        