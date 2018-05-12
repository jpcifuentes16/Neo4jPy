# Universidad del Valle de Guatemala
# Algoritmos y estructura de datos
# Hoja de Trabajo 10: Recomendaciones
# Fecha: XX/05/2018
# Colaboradores:
    # Javier Carpio - 17077
    # Jose Cifuenres - 17509
    # Oscar Juarez - 17315

from Implementacion import *


#___________Declaracion de variables__________#

menu = "\nLa lista de funciones es:\n1. Ingresar un doctor. \n2. Ingresar un paciente. \n3. Paciente dado visita a doctor. \n4. Consultar doctores con una especialidad. \n5. Ingresar que una perosna conoce a otra. \n6. Salir del programa.\n"
listaPacientes = {}
listaDoctores = {}

#Programa principal

while True:

    print (menu)
    seleccion = input("Ingrese la accion que desea realizar: ")

    if (seleccion=="1"):

        #Ingresar un doctor
        nombreDoc = input ("\nIngrese el nombre del doctor: ")
        especialidad = input("Ingrese la especialidad: ")
        colegiado = input ("Ingrese el colegiado: ")
        telefonoDoc = input("Ingrese el numero de telefono: ")

        ingresarDoctor(nombreDoc,especialidad,telefonoDoc,colegiado)

    elif (seleccion=="2"):

        #Ingresar un paciente
        nombrePac = input ("\nIngrese el nombre del paciente: ")
        telefonoPac = input("Ingrese el numero de telefono: ")

        ingresarPaciente(nombrePac,telefonoPac)

    elif (seleccion=="3"):

        #Paciente visita a un doctor
        visitaDoc()

    elif (seleccion=="4"):
        especialidad=input("Ingrese que tipo de especialidad busca en el doctor: ")
        buscarDocPorEspecialidad(especialidad)
        

    elif (seleccion=="5"):

        #Una persona conoce a otra
        crearRelacionesEntrePersonas()

    elif (seleccion=="6"):

        #Salir del programa
        print ("Saliendo del maravilloso programa...")
        break;

    else:
        print ("\nDato inválido, vuelva a intentarlo.")
        

        
        
