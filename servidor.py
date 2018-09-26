from socket import *
from threading import Thread
import random

def atende (conn, cliente):
        while True:
                data = conn.recv (4096)

                if not data or len(data) == 0:
                        break

                print (str(cliente)+" me mandou "+data.decode("utf-8") )
                t = ["Pedra","Papel", "Tesoura"]
     
                escolha_servidor = random.choice(t)
                if escolha_servidor == "Pedra" and data.decode("utf-8") == "Tesoura":
                    conn.send (str.encode ("Você Perdeu!!\nEu escolhi "+escolha_servidor+"\nVocê escolheu: "+data.decode("utf-8") , "UTF-8"))
                elif escolha_servidor == "Papel" and data.decode("utf-8") == "Tesoura":
                    conn.send (str.encode ("Você Ganhou!!\nEu escolhi "+escolha_servidor+"\nVocê escolheu: "+data.decode("utf-8") , "UTF-8"))
                elif escolha_servidor == "Tesoura" and data.decode("utf-8") == "Tesoura":
                    conn.send (str.encode ("Empatou!!\nEu escolhi "+escolha_servidor+"\nVocê escolheu: "+data.decode("utf-8") , "UTF-8"))
                elif escolha_servidor == "Pedra" and data.decode("utf-8") == "Pedra":
                    conn.send (str.encode ("Empatou!!\nEu escolhi "+escolha_servidor+"\nVocê escolheu: "+data.decode("utf-8") , "UTF-8"))
                elif escolha_servidor == "Papel" and data.decode("utf-8") == "Pedra":
                    conn.send (str.encode ("Você Perdeu!!\nEu escolhi "+escolha_servidor+"\nVocê escolheu: "+data.decode("utf-8") , "UTF-8"))
                elif escolha_servidor == "Tesoura" and data.decode("utf-8") == "Pedra":
                    conn.send (str.encode ("Você ganhou!!\nEu escolhi "+escolha_servidor+"\nVocê escolheu: "+data.decode("utf-8") , "UTF-8"))
                elif escolha_servidor == "Pedra" and data.decode("utf-8") == "Papel":
                    conn.send (str.encode ("Você Ganhou!!\nEu escolhi "+escolha_servidor+"\nVocê escolheu: "+data.decode("utf-8") , "UTF-8"))
                elif escolha_servidor == "Papel" and data.decode("utf-8") == "Papel":
                    conn.send (str.encode ("Empatou!!\nEu escolhi "+escolha_servidor+"\nVocê escolheu: "+data.decode("utf-8") , "UTF-8"))
                elif escolha_servidor == "Tesoura" and data.decode("utf-8") == "Papel":
                    conn.send (str.encode ("Você Perdeu!!\nEu escolhi "+escolha_servidor+"\nVocê escolheu: "+data.decode("utf-8") , "UTF-8"))



        print ("Fim da conexao com "+str(cliente))

        conn.close
        

s = socket ()

host = "10.10.14.39"
porta = 8753
s.bind ((host, porta))
s.listen (10)
nthr = 0

while True:
        (conn, cliente) = s.accept ()

        print ("Recebi a conexao de "+str(cliente))
        nthr += 1
        print ("Criando thread "+str(nthr))
        t = Thread(target=atende,args=(conn, cliente,))
        t.start()
