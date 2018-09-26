from socket import  *
import random

s = socket ()

t = ["Pedra","Papel", "Tesoura"]
for x in range(0, 4):
	minhastr = random.choice(t)
	print(minhastr)
	meusbytes=str.encode (minhastr, "UTF-8")
	
	s.connect(("10.10.14.39", 8753))
	s.send (meusbytes)
	data = s.recv (1024)
	print (data.decode("utf-8"))
	s.close ()

