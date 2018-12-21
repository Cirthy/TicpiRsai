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

	print("#\n#    Serveur lancé avec succes. En attente de connexion    ",end='')
	pid = os.fork() # Affichage de l'attente de connexion
	if(not pid):
		while(1):
			sys.stdout.write('\b\b\b.  ')
			sys.stdout.flush()
			time.sleep(0.7)
			sys.stdout.write('\b\b\b.. ')
			sys.stdout.flush()
			time.sleep(0.7)
			sys.stdout.write('\b\b\b...')
			sys.stdout.flush()
			time.sleep(0.7)
	connexion,tsap_client = s.accept()
	os.kill(pid, 15)
	sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b                           ')
	sys.stdout.flush()

	print("\n#    " + str(tsap_client) + " est connecté.\n#\n#")

	connexion.sendall((config.p*config.q).to_bytes(512, byteorder='big', signed=False))
	config.n_distant = int.from_bytes(connexion.recv(512), byteorder='big')


	# les deux ligne suivantes règle un problème d'affichage car la reception du n_distant affiche 4 retours a la ligne
	display_banner()
	print("#\n#    Serveur lancé avec succes.")
	print("#    " + str(tsap_client) + " est connecté.\n#\n#")

	return connexion


def client_start():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	print("#\n#    Sur quelle adresse souhaitez-vous vous connecter ? ",end='')
	ip = input()

	tsap_server = (ip,config.PORT_NUMBER)
	s.connect(tsap_server)

	print("#    Connecté a "+ ip + ".\n#\n#")

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
