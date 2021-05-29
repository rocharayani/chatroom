import socket
import sys
import time

s = socket.socket()
cliente = input(str("Digite seu nome: "))
host = input(str("Por favor, inclua o hostname do servidor: ")) #Pede o nome do host, para realizar a conexão do servidor, tbm poderia pedir o Ip, tanto faz.

port = 8080 #especifica a porta que ja consta no servidor para estabelecer a conexão
#não pode ser uma outra porta pois nosso servidor esta escutando nessa porta

s.connect((host,port))#solicita a conexão e passa os parametros para estabelecer essa conexão
#novamente em 2 parenteses pois recebe um unico parametro

print("Chat server conectado") #aqui o Chat esta informando a conexão

#Essa parte depois do While é igual ao servidor
while 1:
            incoming_message = s.recv(1024) #imprimi o >> para sinalizar ao usuário que o sistema esta pronto para enviar mensagens
            incoming_message = incoming_message.decode()#A variavel incoming é decodificada 
            print(" Servidor : ", incoming_message)#printa a mensagem recebida na tela
            print("")
            message = input(str(">> "))#imprimi o >> para sinalizar ao usuário que o sistema esta pronto para enviar mensagens
            message = message.encode()#codifica a mensagem digitada
            s.send(message)#significa que a conexão esta sendo enviada
            print("mensagem enviada...")
            print("")

.
