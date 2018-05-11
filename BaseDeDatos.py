from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="odiofisica")

doctor = db.labels.create("Doctor")
paciente = db.labels.create("Paciente")
medicina = db.labels.create("Medicina")
visita = db.labels.create("Visita")

#TODOS LOS DOCTORES
Oscar = db.nodes.create(name="Oscar",especialidad="Pediatra",colegiado="5359",telefono="1234")
Jose = db.nodes.create(name="Jose",especialidad="Ninguna",colegiado="5359",telefono="5678")
Javier = db.nodes.create(name="Javier",especialidad="Todas",colegiado="5359",telefono="9102")

doctor.add(Oscar,Jose,Javier)

# Paciente 1

p1 = db.nodes.create(name="Paciente1", numero= "8888")
paciente.add(p1)
 
p1.relationships.create("Visits", Oscar)


# Paciente 2

p2 = db.nodes.create(name="Paciente2", numero= "7777")
paciente.add(p2)
 
p2.relationships.create("Visits", Javier)


#Paciente 1 conoce a paciente 2

p1.relationships.create("Knows",p2)
