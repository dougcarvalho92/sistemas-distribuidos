from socket import *
from threading import Thread

def responde (conn, cliente):
	while True:
		data = conn.recv(4096)
		conn.send("teste")

	conn.close()

s = socket()
host = "10.10.14.39"
porta = 8753
s.bind ((host, porta))
s.listen (10)
while True:
        (conn, cliente) = s.accept ()
        print ("Recebi a conexao de "+str(cliente))
        t = Thread(target=responde,args=(conn, cliente,))
        t.start()