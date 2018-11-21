#!/usr/bin/python3

import os, sys, readline, io, select, curses

from  prime_generator  import *
from  rsa              import *
from  display          import *
from  server           import *

def read_char(stdscr):
	"""checking for keypress"""
	stdscr.nodelay(True)  # do not wait for input when calling getch
	return stdscr.getch()





# Chargement du programme
pid = os.fork()
if not pid :
	display_waiting_vitevite()
config.p = random_prime(config.PRIME_SIZE)
config.q = random_prime(config.PRIME_SIZE)
os.kill(pid, 9)
# Chargementy terminer


index = 0
quit = False

while(not quit):
	display_banner()
	print("#\n#    Ticpirsai est pret a établir une conection :\n#")
	display_menu(index)
	print('\n\n\n')
	pressed = curses.wrapper(read_char)
	if (pressed != -1):
		if (pressed == 27): # touches dirrectionelles
			pressed = curses.wrapper(read_char)
			pressed = curses.wrapper(read_char)
			if (pressed == 65):# UP
				index-=1
			if (pressed == 66):# DOWN
				index+=1
		if (pressed == 10):#ENTER
			if (index%4==0):#démarrage serveur
				display_banner()
				s = server_start(8790)
				chat_run(s)
				quit = True
			if (index%4==1):#connexion client
				display_banner()
				s = client_start()
				chat_run(s)
				quit = True
			if (index%4==2):#crédits
				pass
			if (index%4==3):#quit
				quit = True

	time.sleep(0.1)





print('\n\n')


'''
cypher = encrypt(input("Enter message : "), config.p * config.q)
plain = decrypt(cypher, config.p, config.q)
print("cypher = " + str(cypher) + "\nplain : " + plain)
'''

