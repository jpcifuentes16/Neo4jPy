
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
            
            q = 'MATCH (u:Doctor) WHERE u.Name="'+nombreDoc+'" RETURN u'
            doctor3 = db.query(q, returns=(client.Node))
            
            k = 'MATCH (u:Paciente) WHERE u.Name="'+nombrePac+'" RETURN u'
            pacientes = db.query(k, returns=(client.Node))


            #Se crea el nodo de la fecha en que se realizo la consulta
            fecha = input ("\nIngrese la fecha de consulta: ")
            '''
            nodoFecha = db.nodes.create(Fecha=fecha)
            fecha = db.labels.create("Fecha")
            fecha.add(nodoFecha)
'''

            #Se ingresan los datos de la prescripcion
            nombreMed = input ("Ingrese la medicina recetada al paciente: ")
            fechaInicio = input ("Ingrese la fecha de inicio del tratamiento: ")
            fechaFin = input ("Ingrese la fecha del fin del tratamiento: ")
            dosis = input ("Ingrese la dosis recetada: ")    

            #Se crea el nodo de la medicina
            nodoMedicina = db.nodes.create(Name=nombreMed,desdeFecha=fechaInicio,hastaFecha=fechaFin,Dosis=dosis)
            medicina.add(nodoMedicina)

            
           

            

            for r in doctor3:
                for i in pacientes:
                    #Se crea las relaciones de los nodos
                    i[0].relationships.create("Visits", r[0])
                    i[0].relationships.create("Takes", nodoMedicina)
                    r[0].relationships.create("Prescribe", nodoMedicina)
                    
            break
        

    


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
        
def imprimrPersonas():
    q = 'MATCH (u:Paciente) RETURN u'
    pacientes = db.query(q, returns=(client.Node))

    contador = 0

    print ("\nLa lista de personas es la siguiente:")
    for r in pacientes:
        contador += 1
        print( "%s. " "%s" % (contador, r[0]["Name"]))

    q = 'MATCH (u:Doctor) RETURN u'
    pacientes = db.query(q, returns=(client.Node))

    for r in pacientes:
        contador += 1
        print( "%s. " "%s" % (contador, r[0]["Name"]))
    

def buscarDocPorEspecialidad(especialidad):
    q = 'MATCH (u:Doctor) WHERE u.Especialidad="'+especialidad+'" RETURN u'
    pacientes = db.query(q, returns=(client.Node))

    contador = 0

    print ("\nLa lista de doctores es la siguiente:")
    for r in pacientes:
        contador += 1
        print( "%s. " "%s" % (contador, r[0]["Name"]))

    if(contador==0):
        print("No hay ningun doctor con dicha especialidad")


def crearRelacionesEntrePersonas():
    imprimrPersonas()
    control1=""
    while True:
        
        nombrePer1 = input("\nPor favor ingrese el nombre de la persona: ")

        q = 'MATCH (u:Paciente) WHERE u.Name="'+nombrePer1+'" RETURN u'
        posPersonas1 = db.query(q, returns=(client.Node))

        k = 'MATCH (u:Doctor) WHERE u.Name="'+nombrePer1+'" RETURN u'
        posPersonas2 = db.query(k, returns=(client.Node))

        if (not posPersonas1):
            control1="Paciente"          
        else:
            control1="Paciente"
            break
            
        if (not posPersonas2):
            control1="Doctor"
        else:
            control1="Doctor"
            break
        print ("La persoana ingresado no existe en la lista!")

    print(control1)
    control2=""
    while True:
        
        nombrePer2 = input("\nIngrese a la persona que conoce "+nombrePer1+" : ")

        q = 'MATCH (u:Paciente) WHERE u.Name="'+nombrePer2+'" RETURN u'
        posPersonas1 = db.query(q, returns=(client.Node))

        k = 'MATCH (u:Doctor) WHERE u.Name="'+nombrePer2+'" RETURN u'
        posPersonas2 = db.query(k, returns=(client.Node))

        

        if (not posPersonas1):
            control2="Paciente"           
        else:
            control2="Paciente"
            break
            
        if (not posPersonas2):
            control2="Doctor"
        else:
            control2="Doctor"
            break
        print ("La persoana ingresado no existe en la lista!")
    print(control2)

    q = 'MATCH (u:'+control1+') WHERE u.Name="'+nombrePer1+'" RETURN u'
    Qpersona1 = db.query(q, returns=(client.Node))
            
    k = 'MATCH (u:'+control2+') WHERE u.Name="'+nombrePer2+'" RETURN u'
    Qpersona2 = db.query(k, returns=(client.Node))

    for r in Qpersona1:
        for i in Qpersona2:
            #Se crea las relaciones de los nodos
            r[0].relationships.create("Knows", i[0])

def getDocPorEspecialidad(especialidad):
    q = 'MATCH (u:Doctor) WHERE u.Especialidad="'+especialidad+'" RETURN u'
    pacientes = db.query(q, returns=(client.Node))

    contador = 0
    diccionario={}

    
    for r in pacientes:
        contador += 1
        diccionario[r[0]["Name"]]=0
                
    if(contador==0):
        return False
    else:
        return diccionario

def getConocidos(persona):
    q = 'MATCH (u:Paciente)-[r:Knows]->(m:Paciente) WHERE u.Name="'+persona+'" RETURN u, type(r), m'
    conocidos = db.query(q, returns=(client.Node, str, client.Node))

    contador = 0
    lista=[]
    conocidos2=[]
    
    
    for r in conocidos:
        contador += 1
        lista.append(r[2]["Name"])
        conocidos2.append(r[2]["Name"])

    for i in lista:
        q = 'MATCH (u:Paciente)-[r:Knows]->(m:Paciente) WHERE u.Name="'+i+'" RETURN u, type(r), m'
        conocidos = db.query(q, returns=(client.Node, str, client.Node))

        for r in conocidos:
            contador += 1
            conocidos2.append(r[2]["Name"])
    print(conocidos2)
    return conocidos2
    
    

def recomendacion1():
    imprimirPacientes()
    while True:
        
        nombrePac = input("\nPor favor ingrese el nombre del paciente: ")

        q = 'MATCH (u:Paciente) WHERE u.Name="'+nombrePac+'" RETURN u'
        pacientes = db.query(q, returns=(client.Node))

        if (not pacientes):
            print ("El paciente ingresado no existe en la lista!")            
        else:            
            break

    while True:
        especialidad=input("Ingrese la especialidad de doctor que necesita: ")
        if(getDocPorEspecialidad(especialidad)!=False):
            listaDoc=getDocPorEspecialidad(especialidad)
            print(listaDoc)
            break

    print(nombrePac)
    conocidosLista=getConocidos(nombrePac)

    for i in conocidosLista:
        q = 'MATCH (u:Paciente)-[r:Visits]->(m:Doctor) WHERE u.Name="'+i+'" RETURN u, type(r), m'
        conocidos = db.query(q, returns=(client.Node, str, client.Node))

        for r in conocidos:
            if(r[2]["Name"] in listaDoc):
                listaDoc[r[2]["Name"]]=listaDoc[r[2]["Name"]]+1
            
    print(listaDoc)


    listaCoincidencias=[]

    for i in listaDoc.values():
        listaCoincidencias.append(i)

    listaCoincidencias.sort(reverse=True)
    


    sugerencia=[]
    for x in listaDoc:
        if(listaDoc[x]==listaCoincidencias[0]):
            listaCoincidencias.pop(0)
            sugerencia.append(x)
            
    return sugerencia
