import pyrebase
import json
from collections import OrderedDict
import os


config = {
  "apiKey": "AIzaSyBA6toEeoJ4p3DTU1pEed1RFp6v0pAizdc",
  "authDomain": "apirest-projeto.firebaseapp.com",
  "databaseURL": "https://apirest-projeto.firebaseio.com",
  "storageBucket": "apirest-projeto.appspot.com",
  "serviceAccount": "apirest-projeto-firebase-adminsdk-lnlj2-26e8336c87.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

def get(numid):
	flag = True
	if numid == "":
		produtos = db.child("/").get()
		print (json.dumps(produtos.val(), indent=4))
	else:
		produtos = db.child("produto").get()
		dic = produtos.val()
		for i in dic:
			if dic[i]["id"] == numid:
				print (json.dumps(dic[i], indent=4))
				print("\n")
				flag = False
		if flag:
			print("\n")
			print("Produto inexistente")
			print("\n")

def post(nome, desc, qtd, valor, link):
	num_id = db.child("num_Produtos/").get()
	print(num_id.val())
	data = {"id": num_id.val(),"nome":nome,"descricao": desc,"estoque": qtd,"preco":valor,"link":link}
	db.child("produto").push(data)
	db.child("/").update({"num_Produtos": num_id.val()+1})
	print ("Elemento Adicionado com sucesso")
	print("\n")


def remove(numid):
	flag = True

	if numid == "":
		print("insira um id contido no banco")
	else:
		produtos = db.child("produto").get()
		dic = produtos.val()
		for i in dic:
			if dic[i]["id"] == numid:
				db.child("produto").child(i).remove()
				print ("Elemento removido com sucesso")
				print("\n")
				flag = False
		if flag:
			print("\n")

			print("Produto inexistente")
			print("\n")


def put(numid,nome, desc, qtd, valor, link):
	flag = True

	if numid == "":
		print("insira um id contido no banco")
	else:
		produtos = db.child("produto").get()
		dic = produtos.val()
		for i in dic:
			if dic[i]["id"] == numid:
				db.child("produto").child(i).update({"id": numid,"nome":nome,"descricao": desc,"estoque": qtd,"preco":valor,"link":link})
				print("Elemento Atualizado com sucesso")
				print("\n")
				flag = False
		if flag:
			print("\n")
			print("Produto inexistente")
			print("\n")


def main():
	os.system('clear') or None

	print("--------------------- MENU ---------------------")
	print("\n")
	print("Escolha a opção que desejar:")
	print("\n")
	print("[1] Listar produtos")
	print("[2] Listar produto")
	print("[3] Inserir produto")
	print("[4] Atualizar Produto")
	print("[5] Remover Produto")
	print("\n")

	resposta = int(input("Informe a operação: "))
	os.system('clear') or None

	if resposta == 1:
		get("");
		resposta = input("Deseja realizar outra operação <s/n>:  ")
		reposta = resposta.upper()
		if reposta == "S":
			os.system('clear') or None
			return main()
		else:
			quit()
	
	elif resposta == 2:
		numid = int(input("Informe o numero do id do produto que deseja consultar: "))
		get(numid)
		resposta = input("Deseja realizar outra operação <s/n>:  ")
		reposta = resposta.upper()
		if reposta == "S":
			os.system('clear') or None
			return main()
		else:
			quit()
			
	elif resposta == 3:
		print("Complete os dados, para poder inserir o produto")
		print("\n")
		nome = input("Informe o nome para o produto:  ")
		descricao = input("Informe a descricao do produto:  ")
		qtd = int(input("Informe a quantidade em estoque:  "))
		valor = int(input("Informe o valor para o produto:  "))
		link = input("Informe o link para a imagem do produto na web:  ")
		if(qtd < 0 or valor < 0):
			print("Entradas incorretas")	
		else:
			post(nome,descricao,qtd,valor,link)

		resposta = input("Deseja realizar outra operação <s/n>:  ")
		reposta = resposta.upper()
		if reposta == "S":
			os.system('clear') or None
			return main()
		else:
			quit()
	
	elif resposta == 4:
		print("Complete os dados, para poder alterar o produto")
		print("\n")
		numid = int(input("Informe o numero do id do produto que deseja alterar: "))
		nome = input("Informe o nome para o produto:  ")
		descricao = input("Informe a descricao do produto:  ")
		qtd = int(input("Informe a quantidade em estoque:  "))
		valor = int(input("Informe o valor para o produto:  "))
		link = input("Informe o link para a imagem do produto na web:  ")
		if(qtd < 0 or valor < 0):
			print("Entradas incorretas")	
		else:
			put(numid,nome,descricao,qtd,valor,link)
		resposta = input("Deseja realizar outra operação <s/n>:  ")
		reposta = resposta.upper()
		if reposta == "S":
			os.system('clear') or None
			return main()
		else:
			quit()

	elif resposta == 5:
		numid = int(input("Informe o numero do id do produto que remover: "))
		remove(numid)
		resposta = input("Deseja realizar outra operação <s/n>:  ")
		reposta = resposta.upper()
		if reposta == "S":
			os.system('clear') or None
			return main()
		else:
			quit()

main()
