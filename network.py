#!/usr/bin/python3

import socket
import os
import sys
import time
import config
from   display   import *
from   rsa		import *



def server_start():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Le port redevient utilisable tout de suite après avoir été fermé

	s.bind(('',config.PORT_NUMBER))
	s.listen(1)
	print("#                                                                                                 #")
	pid = os.fork() # Affichage de l'attente de connexion
	if(not pid):
		while(1):
			sys.stdout.write('\r#    Serveur lancé avec succes. En attente de connexion .                                         #')
			sys.stdout.flush()
			time.sleep(0.7)
			sys.stdout.write('\r#    Serveur lancé avec succes. En attente de connexion ..                                        #')
			sys.stdout.flush()
			time.sleep(0.7)
			sys.stdout.write('\r#    Serveur lancé avec succes. En attente de connexion ...                                       #')
			sys.stdout.flush()
			time.sleep(0.7)
	connexion,tsap_client = s.accept()
	os.kill(pid, 15)

	connexion.sendall((config.p*config.q).to_bytes(512, byteorder='big', signed=False))
	config.n_distant = int.from_bytes(connexion.recv(512), byteorder='big')


	# les deux ligne suivantes règlent un problème d'affichage car la reception du n_distant affiche 4 retours a la ligne
	display_banner()
	print("#                                                                                                 #")
	print("\r#    Serveur lancé avec succes.                                                                   #")
	print("#    " + str(tsap_client) + " est connecté.", end='')
	for i in range(79-len(str(tsap_client))):
		print(" ",end='')
	print("#")
	print("#                                                                                                 #")
	#--------------------------------------------------------------------------------------------------------------------


	return connexion




def client_start():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	conectionError = False
	while True:
		display_banner()
		if (conectionError):
			print("#    Erreur de connexion.                                                                         #")
		else:
			print("#                                                                                                 #")
		
		print("#    Sur quelle adresse souhaitez-vous vous connecter ? ",end='')
		ip = input()
		tsap_client = (ip,config.PORT_NUMBER)

		try:
			s.connect(tsap_client)
		except socket.error:
			conectionError = True
			continue
		break

	display_banner()
	print("#                                                                                                 #")
	print("#    Connecté a " + ip + ".", end='')
	for i in range(81-len(str(ip))):
		print(" ",end='')
	print("#")
	print("#                                                                                                 #")



	config.n_distant = int.from_bytes(s.recv(512), byteorder='big')
	s.sendall((config.p*config.q).to_bytes(512, byteorder='big', signed=False))

	return s


def chat_run(s):

	pid = os.fork()
	print('#    =>',end='')

	while 1:
		if not pid:
			#enfant
			recu = s.recv(512)
			recu_cipher = int.from_bytes(recu, byteorder='big')
			recu_plain = decrypt(recu_cipher)

			print('\b\b\b\b\b\b\b\b\b',end='')
			for i in range(93-len(recu_plain)):
				print(' ',end='')
			print(recu_plain + '\n#    =>',end='')

		else:
			#parent
			envoi_plain = input("")
			if (envoi_plain == 'quit' or envoi_plain == 'exit'):
				os.kill(pid, 9) # terminaison du processus enfant
				s.close()
				sys.exit(0)
			envoi_cypher = encrypt(envoi_plain)
			envoi = envoi_cypher.to_bytes(512, byteorder='big', signed=False)
			print('#    =>',end='')
			s.sendall(envoi)
