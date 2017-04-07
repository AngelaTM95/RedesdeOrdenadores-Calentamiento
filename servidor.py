#!/usr/bin/python
import socket
import os
import sys

arglen=len(sys.argv)
if arglen < 2 :
    print('Please run as "servidor puerto fichero-de-mensajes"')
    exit()

fo = open(sys.argv[2],"r")
s = socket.socket()
port = int(sys.argv[1])
s.bind(('', port))
s.listen(1)
sc, addr = s.accept() #conexion y direccion de cliente

while  True:
	tipo = sc.recv(1024)

	if tipo == 'udp':
		reci = sc.recv(1024)
		print "",reci
		linea = fo.readline()
		sc.send(linea)
		exit()
	if tipo == 'tcp':	
		recibido = sc.recv(1024)
		print  "", recibido
		linea = fo.readline()
		sc.send(linea)
		
	
sc.close()
s.close()
fo.close()
#os.remover("provervio.txt")
