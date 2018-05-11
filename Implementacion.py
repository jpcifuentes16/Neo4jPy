# Universidad del Valle de Guatemala
# Algoritmos y estructura de datos
# Hoja de Trabajo 10: Recomendaciones
# Fecha: XX/05/2018
# Colaboradores:
    # Javier Carpio - 17077
    # Jose Cifuenres - 17509
    # Oscar Juarez - 17315

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client


db = GraphDatabase("http://localhost:7474", username="neo4j", password="odiofisica")

doctor = db.labels.create("Doctor")
paciente = db.labels.create("Paciente")
medicina = db.labels.create("Medicina")
visita = db.labels.create("Visita")


def ingresarDoctor(nombre,especialidad,colegiado,telefono):

    nuevoDoc = db.nodes.create(Name = nombre, Especialidad = especialidad, Colegiado = colegiado, Telefono = telefono)
    doctor.add(nuevoDoc)

    print ("\nDoctor agregado con exito!")


def ingresarPaciente(nombre,telefono):

    nuevoPac = db.nodes.create(Name = nombre, Telefono = telefono)
    paciente.add(nuevoPac)

    print ("\nPaciente agregado con exito!")


def visitaDoc():

    imprimirPacientes()

    while True:
        
        nombrePac = input("\nPor favor ingrese el nombre del paciente: ")

        q = 'MATCH (u:Paciente) WHERE u.name="'+nombrePac+'" RETURN u'
        #pacienteActual = q        
        pacientes = db.query(q, returns=(RAW))

        if (not pacientes):
            print ("El paciente ingresado no existe en la lista!")
            
        else:
            pacienteActual = paciente[0]      
            break;


    imprimirDoctores()
    
    while True:

        nombreDoc =input("\nPor favor ingrese el nombre del doctor: ")

        q = 'MATCH (u:Doctor) WHERE u.name="'+nombreDoc+'" RETURN u'
        doctores = db.query(q, returns=(client.Node))

        if (not doctores):
            print ("El doctor ingresado no existe en la lista!")
        else:
            doctorActual = doctores[0]
            break;
        

    #Se crea el nodo de la fecha en que se realizo la consulta
    fecha = input ("\nIngrese la fecha de consulta: ")
    nodoFecha = db.nodes.create(Fecha=fecha)


    #Se ingresan los datos de la prescripcion
    nombreMed = input ("Ingrese la medicina recetada al paciente: ")
    fechaInicio = input ("Ingrese la fecha de inicio del tratamiento: ")
    fechaFin = input ("Ingrese la fecha del fin del tratamiento: ")
    dosis = input ("Ingrese la dosis recetada: ")    

    #Se crea el nodo de la medicina
    nodoMedicina = db.nodes.create(Name=nombreMed,desdeFecha=fechaInicio,hastaFecha=fechaFin,Dosis=dosis)
    medicina.add(nodoMedicina)

    #Se crea las relaciones de los nodos
    pacienteActual.relationships.create("Takes", nodoMedicina)
    doctorActual.relationships.create("Prescribe", nodoMedicina)


def imprimirPacientes():

    q = 'MATCH (u:Paciente) RETURN u'
    pacientes = db.query(q, returns=(client.Node))

    contador = 0

    print ("\nLa lista de pacientes es la siguiente:")
    for r in pacientes:
        contador += 1
        print( "%s. " "%s" % (contador, r[0]["name"]))


def imprimirDoctores():

    q = 'MATCH (u:Doctor) RETURN u'
    pacientes = db.query(q, returns=(client.Node))

    contador = 0

    print ("\nLa lista de doctores es la siguiente:")
    for r in pacientes:
        contador += 1
        print( "%s. " "%s" % (contador, r[0]["name"]))
