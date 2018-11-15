#!/usr/bin/python3


import socket, os, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('',8790))
s.listen(1)
connexion,tsap_client = s.accept()

print(tsap_client)

pid = os.fork()
while 1:
	if not pid:
		#enfant
		recu = connexion.recv(1024)
		
	else:
		#parent
		envoi = ""
		if envoi == 'Q':
			os.kill(pid, 9) # terminaison du processus enfant
			connexion.close()
			sys.exit(0)


		
		connexion.sendall(envoi.encode('utf-8'))
	

