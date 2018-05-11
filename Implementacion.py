
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
fecha = db.labels.create("Fecha")

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

        q = 'MATCH (u:Paciente) WHERE u.Name="'+nombrePac+'" RETURN u'
        pacientes = db.query(q, returns=(client.Node))

        if (not pacientes):
            print ("El paciente ingresado no existe en la lista!")
            
        else:
            
            break;


    imprimirDoctores()
    
    while True:

        nombreDoc =input("\nPor favor ingrese el nombre del doctor: ")

        q = 'MATCH (u:Doctor) WHERE u.Name="'+nombreDoc+'" RETURN u'
        doctores = db.query(q, returns=(client.Node))

        if (not doctores):
            print ("El doctor ingresado no existe en la lista!")
        else:
            #nombrePac
            #nombreDoc
            #p2.relationships.create("Visits", Javier)

            q = 'MATCH (u:Doctor) WHERE u.Name="'+nombreDoc+'" RETURN u'
            doctor3 = db.query(q, returns=(client.Node))         

    
            for r in doctor3:
                nombre=r[0]["Name"]
                colegiado=r[0]["Colegiado"]
                especialidad=r[0]["Especialidad"]
                telefono=r[0]["Telefono"]
                break


            k = 'MATCH (u:Paciente) WHERE u.Name="'+nombrePac+'" RETURN u'
            pacientes = db.query(k, returns=(client.Node))

    
   
            for i in pacientes:
            
                
                nombre2=i[0]["Name"]
                numero=i[0]["numero"]
                break
                
            Doc2 = db.nodes.create(Name=nombre,Especialidad=especialidad,Colegiado=colegiado,Telefono=telefono)
            doctor.add(Doc2)

            Pac2= db.nodes.create(Name=nombre2, numero=numero)
            paciente.add(Pac2)

            Pac2.relationships.create("Visits", Doc2)
   
            

            break
        

    #Se crea el nodo de la fecha en que se realizo la consulta
    fecha = input ("\nIngrese la fecha de consulta: ")
    nodoFecha = db.nodes.create(Fecha=fecha)
    fecha.add(nodoFecha)


    #Se ingresan los datos de la prescripcion
    nombreMed = input ("Ingrese la medicina recetada al paciente: ")
    fechaInicio = input ("Ingrese la fecha de inicio del tratamiento: ")
    fechaFin = input ("Ingrese la fecha del fin del tratamiento: ")
    dosis = input ("Ingrese la dosis recetada: ")    

    #Se crea el nodo de la medicina
    nodoMedicina = db.nodes.create(Name=nombreMed,desdeFecha=fechaInicio,hastaFecha=fechaFin,Dosis=dosis)
    medicina.add(nodoMedicina)

    #Se crea las relaciones de los nodos
    Pac2.relationships.create("Takes", nodoMedicina)
    Doc2.relationships.create("Prescribe", nodoMedicina)
    Doc2.relationships.create("Visits", nodoFecha)
    nodoFecha.relationships.create("Visits", Pac2)


def imprimirPacientes():

    q = 'MATCH (u:Paciente) RETURN u'
    pacientes = db.query(q, returns=(client.Node))

    contador = 0

    print ("\nLa lista de pacientes es la siguiente:")
    for r in pacientes:
        contador += 1
        print( "%s. " "%s" % (contador, r[0]["Name"]))


def imprimirDoctores():

    q = 'MATCH (u:Doctor) RETURN u'
    pacientes = db.query(q, returns=(client.Node))

    contador = 0

    print ("\nLa lista de doctores es la siguiente:")
    for r in pacientes:
        contador += 1
        print( "%s. " "%s" % (contador, r[0]["Name"]))
