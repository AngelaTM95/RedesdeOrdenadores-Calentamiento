#!/usr/bin/python

import socket
import sys 
import os

arglen=len(sys.argv)
if arglen < 3 :
    print('Please run as "cliente -(udp|tcp) ip_servidor puerto"')
    exit()

s = socket.socket()
port = int(sys.argv[3])
ip = sys.argv[2]
s.connect(( ip,  port))

while  True:
	tipo = sys.argv[1]
	s.send (tipo)

	if tipo == 'udp':
		mensaje = "Conexion establecida con servidor udp"
 		s.send(mensaje)
		linea=s.recv(1024)
		print " ",linea
		exit()
		

	if tipo == 'tcp':
 		mensaje = "Conexion establecida con servidor tcp"
 		s.send(mensaje)
		linea=s.recv(1024)
		print "",linea
		msg=raw_imput("Desea seguir con la conexion?: ")
		if msg == "si":
			break
		
s.close()	





