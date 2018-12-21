#!/usr/bin/python3

import	os, sys, readline, io, select, curses, random

from	prime_generator	import *
from	rsa				import *
from	display			import *
from	server			import *



def read_char(stdscr):
	"""checking for keypress"""
	stdscr.nodelay(True)  # do not wait for input when calling getch
	return stdscr.getch()


# Chargement du programme (génération des clés)
pid = os.fork() # Un processus fait un affichage pendant que l'autre génère les nombres premiers
if not pid :
	display_waiting_vitevite()
config.p = random_prime(config.PRIME_SIZE_P)
while(ecgd((config.p - 1) * (config.q - 1), config.e)[0] != 1): # e doit être premier avec phi(n)
	config.q = random_prime(config.MIN_PRIME_SIZE_Q + random.randrange(AMPL_PRIME_SIZE_Q))
config.d = modinv(config.e, (config.p - 1) * (config.q - 1))
os.kill(pid, 9) # Chargement terminé

index = 0

while(True):
	display_banner()
	print("#\n#    Ticpirsai est prêt à établir une connection :\n#")
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
				s = server_start(8790)
				chat_run(s)
				break
			if (index%4==1): # connexion client
				display_banner()
				s = client_start()
					chat_run(s)
				break
			if (index%4==2): # crédits
				display_banner()
				break
			if (index%4==3): # quit
				break
	time.sleep(0.1) # refresh pour l'attente d'une entrée

print('\n\n')

'''
cypher = encrypt(input("Enter message : "), config.p * config.q)
plain = decrypt(cypher, config.p, config.q)
print("cypher = " + str(cypher) + "\nplain : " + plain)
'''