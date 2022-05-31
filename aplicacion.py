# -*- coding: utf-8 -*-
"""
Created on Mon May 30 12:06:50 2022

@author: PIERO
"""
# ALUMNO SAYAS DE LA VEGA PIERO GABRIEL
import gestion_archivos


# ALUMNO SAYAS DE LA VEGA PIERO GABRIEL
def menu():
    print("****** menu principal*********")
    print("1.crear archivo")
    print("2.eliminar archivo")
    print("3.agregar contenido")
    print("4. mostrar contenido")
    print("5.salir")
 
    
 # ALUMNO SAYAS DE LA VEGA PIERO GABRIEL
def crear():
    print("---Crear archivos---")
    archivo= input("Archivo: ")
    contenido=input("contenido: ")
    gestion_archivos.crear_archivo(archivo, contenido)
  
    
  # ALUMNO SAYAS DE LA VEGA PIERO GABRIEL
def eliminar():
    print("----Eliminar archivo----")
    archivo= input("archivo: ")
    gestion_archivos.eliminar_archivo(archivo)
  
    
  # ALUMNO SAYAS DE LA VEGA PIERO GABRIEL  
def agregar():
    print("------Agregar datos a un archivo------")
    archivo= input("Archivo : ")
    contenido=input("Contenido: ")
    gestion_archivos.agregar_contenido_archivo(archivo, contenido)
  
    # ALUMNO SAYAS DE LA VEGA PIERO GABRIEL
def listar():
    print("---Mostrar contenido de un archivo----")
    archivo= input("Archivo: ")
    print(gestion_archivos.leer_achivo(archivo))
    
    
    # ALUMNO SAYAS DE LA VEGA PIERO GABRIEL
def salir():
    print("Gracias por su visita")
    
    
    # ALUMNO SAYAS DE LA VEGA PIERO GABRIEL
def error():
    print("Opcion incorrecta")
    
opcion=1

while opcion!=5:
    menu()
    opcion=int(input("Digite opcion: "))
    if opcion==1:
        crear()
    elif opcion==2:
        eliminar()
    elif opcion==3:
        agregar()
    elif opcion==4:
        listar()
    elif opcion==5:
        salir()
    else:
        error()
    
    
    
    