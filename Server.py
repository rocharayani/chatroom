import socket #socket: é um modulo que combina um ip e um numero de porta
import sys #contém algumas variáveis e funções relacionadas ao funcionamento do próprio Python no ambiente em que ele está rodando
import time




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Ou seja a conexão será aceita via IPV4 e no protocolo TCP
#pegando a função socket que vai retornar  o metodo socket
#esse "s" poderia ser qualquer coisa, é só uma variavel
host = socket.gethostname()#Esse metodo é responsavel por “pegar” nome do host
print("o servidor irá iniciar no host: ", host)
port = 8080

#usa-se 2 parenteses pois é um unico parametro que é dividido em 2 partes
s.bind((host,port)) #Invocando o metodo bind(que liga o server nesse endereço, vinculando no socket

print("\nO servidor concluiu a ligação ao host e à porta com sucesso")

print("\n...esperando por conexões de entrada")

s.listen(1) #colocando socket no modo de escuta, ou seja, o servidor agora esta aceitando conexões
#O 1 é a quantidade de conexões que ele aceitará

conn, addr = s.accept() #conn e addr significa conexão e endereço, que serão o retorno do s.accept que é o o metodo que aceita a conexão
#o addr na verdade só vamos usar para mostrar na tela qual é o endereço que esta conectado
#usa-se nessa sequencia mesmo pois é o padrão do accept, claro que você pode alterar mas normalmente é usado assim

print(addr, " \nConectou-se ao servidor e agora está online ...")#O addr serve para mostrar qual é o endereço de quem se conectou a rede e vem do parametro acima



while 1:
            message = input(str(">> ")) #imprimi o >> para sinalizar ao usuário que o sistema esta pronto para enviar mensagens
            message = message.encode() #codifica a mensagem digitada

#quando uma mensagem é enviada via socket ela vai em bytes e por isso usamos o decode para decodifica-la, transformar bytes em string
 
            conn.send(message) #significa que a conexão esta sendo enviada
            print("\nmensagem enviada...\n")
            
            incoming_message = conn.recv(1024)#O incoming coloca a conexão dentro de uma varial
            #O recv chama o metodo received com o tamanho maximo dos dados que a gente quer receber em bytes

            incoming_message = incoming_message.decode() #A variavel incoming é decodificada
            print("Cliente : ", incoming_message)#printa a mensagem recebida na tela
            print("")
