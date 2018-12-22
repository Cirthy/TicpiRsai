#!/usr/bin/python3

import	os, sys, readline, io, select, curses, random

from	prime_generator	import *
from	rsa				import *
from	display			import *
from	network			import *



def read_char(stdscr):
	"""checking for keypress"""
	stdscr.nodelay(True)  # do not wait for input when calling getch
	return stdscr.getch()


os.system("clear")
print("Veuillez agrandir la console pour que le programme s'affiche correctement.")
print("Veuillez agrandir la console pour que le programme s'affiche correctement (min 99 colonnes).")
while(True):
	rows, columns = os.popen('stty size', 'r').read().split()
	if(int(rows) > 19 and int(columns) > 98):
		break
	time.sleep(0.1)


# Chargement du programme (génération des clés)
pid = os.fork() # Un processus fait un affichage pendant que l'autre génère les nombres premiers
if not pid :
	display_waiting_vitevite()
config.p = random_prime(config.PRIME_SIZE_P)
while(ecgd((config.p - 1) * (config.q - 1), config.e)[0] != 1): # e doit être premier avec phi(n)
	config.q = random_prime(config.MIN_PRIME_SIZE_Q + random.randrange(config.AMPL_PRIME_SIZE_Q))
config.n_local = config.p * config.q
config.d = modinv(config.e, (config.p - 1) * (config.q - 1))
os.kill(pid, 9) # Chargement terminé

index = 0

while(True):
	display_banner()
	print("#                                                                                                 #")
	print("#    Ticpirsai est prêt à établir une connection :                                                #")
	print("#                                                                                                 #")
	display_menu(index)

	print('\n\n\n')
	pressed = curses.wrapper(read_char) # curses = entrée de touches sans buffer
	if (pressed != -1):
		if (pressed == 27): # 27 <=> touches dirrectionelles
			pressed = curses.wrapper(read_char)
			pressed = curses.wrapper(read_char)
			if (pressed == 65): # UP
				index-=1
			if (pressed == 66): # DOWN
				index+=1
		if (pressed == 10): # ENTER
			if (index%4==0): # démarrage serveur
				display_banner()
				chat_run(server_start())
				break
			if (index%4==1): # connexion client
				display_banner()
				chat_run(client_start())
				break
			if (index%4==2): # crédits
				display_banner()
				display_credits()
			if (index%4==3): # quit
				break
	time.sleep(0.1) # refresh pour l'attente d'une entrée

print('\n\n')

'''
cypher = encrypt(input("Enter message : "), config.p * config.q)
plain = decrypt(cypher, config.p, config.q)
print("cypher = " + str(cypher) + "\nplain : " + plain)
'''