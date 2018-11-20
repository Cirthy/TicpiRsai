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
p, q = random_prime(config.PRIME_SIZE), random_prime(config.PRIME_SIZE)
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
				s,connexion,tsap_client = server_start(8790)
				server_run(s,connexion,tsap_client)
				quit = True
			if (index%4==1):#connexion client
				display_banner()
				client_start()
				client_run()
				quit = True
			if (index%4==2):#crédits
				pass
			if (index%4==3):#quit
				quit = True

	time.sleep(0.1)





print('\n\nindex')



#serveur_start()



print('\n\n')

print(p)
print(q)



cypher = encrypt(input("Enter message : "), p * q)
plain = decrypt(cypher, p, q)
print("cypher = " + str(cypher) + "\nplain : " + plain)

