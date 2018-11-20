#!/usr/bin/python3


import socket, os, sys, time



def server_start(port):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	s.bind(('',port))
	s.listen(1)

	print("#\n#    Serveur lancé avec succes. En attente de connexion    ",end='')
	pid = os.fork()
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

	print("\n#    " + str(tsap_client) + " est connecté.")
	return s,connexion,tsap_client





def server_run(s,connexion,tsap_client):

	pid = os.fork()
	while 1:
		if not pid:
			#enfant
			recu = connexion.recv(1024)
			# 512 suffit
			
		else:
			#parent
			envoi = ""
			if envoi == 'Q':
				os.kill(pid, 9) # terminaison du processus enfant
				connexion.close()
				sys.exit(0)

			connexion.sendall(envoi.encode('utf-8'))


def client_start():
	pass



def client_run():
	pass


