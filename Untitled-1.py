


import pyrebase
import json
from collections import OrderedDict

config = {
  "apiKey": "AIzaSyBA6toEeoJ4p3DTU1pEed1RFp6v0pAizdc",
  "authDomain": "apirest-projeto.firebaseapp.com",
  "databaseURL": "https://apirest-projeto.firebaseio.com",
  "storageBucket": "apirest-projeto.appspot.com",
  "serviceAccount": "apirest-projeto-firebase-adminsdk-lnlj2-26e8336c87.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

db.child("produto").remove()
db.child("num_Produtos").remove()

db.child("/").push({"num_Produtos":9})


data = {"id": 0,"nome":"Garra robotica para servos 9g","descricao": "Garra robotica impressa em ABR aproximadamente 15cm, nao acompanha motores","estoque": 20,"preco":20.00}
db.child("produto").push(data)

data = {"id": 1,"nome":"Plataforma robótica com servos 9g","descricao": "Plataforma impressa em ABR acompanhada de dois servo motores","estoque": 10,"preco":40.00}
db.child("produto").push(data)

data = {"id": 2,"nome":"Mesa linear sem motores","descricao": "Mesa linear impressa em ABR aproximadamente 10cm com um fusos giratorio de aluminio, nao acompanha motores","estoque": 10,"preco":50.00}
db.child("produto").push(data)

data = {"id": 3,"nome":"Kit de montagem open source","descricao": "Kit de montagem open source, acompanha: 1 arduino, uma mini plataforma robotica para micro servos 9g, 2 micro servos, e 1 bateria","estoque": 5,"preco":100.00}
db.child("produto").push(data)

data = {"id": 4,"nome":"Motor de Passo NEMA ","descricao": "Motor de passos nema, original","estoque": 20,"preco":120.00}
db.child("produto").push(data)

data = {"id": 5,"nome":"Raspberry pi 4","descricao": "Placa Raspberry pi 4 original, acompanha cabo de fonte","estoque": 20,"preco":400.00}
db.child("produto").push(data)

data = {"id": 6,"nome":"Arduino Mega","descricao": "Placa Arduino mega original, acompanha cabo de fonte","estoque": 50,"preco":90.00}
db.child("produto").push(data)

data = {"id": 7,"nome":"Arduino Uno","descricao": "Placa Arduino Uno original, acompanha cabo de fonte","estoque": 32,"preco":60.00}
db.child("produto").push(data)

data = {"id": 8,"nome":"Panda Board","descricao": "Placa Panda Board original, acompanha cabo de fonte","estoque": 50,"preco":20.00}
db.child("produto").push(data)



users = db.child("produto").get()

print (json.dumps(users.val(), indent=4))
