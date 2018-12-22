#!/usr/bin/python3

import time
import sys
import os
import config



def display_menu(index):
	index%=4
	if (index==0):
		print("#   --> Démarrer un serveur                                                                       #")
		print("#       Se connecter a un serveur en tant que client                                              #")
		print("#       Crédit                                                                                    #")
		print("#       Quitter                                                                                   #")
	elif (index==1):
		print("#       Démarrer un serveur                                                                       #")
		print("#   --> Se connecter a un serveur en tant que client                                              #")
		print("#       Crédit                                                                                    #")
		print("#       Quitter                                                                                   #")
	elif (index==2):
		print("#       Démarrer un serveur                                                                       #")
		print("#       Se connecter a un serveur en tant que client                                              #")
		print("#   --> Crédit                                                                                    #")
		print("#       Quitter                                                                                   #")
	else:
		print("#       Démarrer un serveur                                                                       #")
		print("#       Se connecter a un serveur en tant que client                                              #")
		print("#       Crédit                                                                                    #")
		print("#   --> Quitter                                                                                   #")


def display_banner():
	os.system("clear")
	print("###################################################################################################")
	print("############################   _____ _            _                _   ############################")
	print("############################  |_   _(_) ___ _ __ (_)_ __ ___  __ _(_)  ############################")
	print("############################    | | | |/ __| '_ \\| | '__/ __|/ _` | |  ############################")
	print("############################    | | | | (__| |_) | | |  \\__ \\ (_| | |  ############################")
	print("############################    |_| |_|\\___| .__/|_|_|  |___/\\__,_|_|  ############################")
	print("############################               |_|                         ############################")
	print("###################################################################################################")
	

def display_waiting_vitevite():
	i=0
	while(1):
		display_progress_vitevite(i%(97+32)-32)
		i+=1


def display_progress_vitevite(n):
	display_banner()
	print("# Chargement du programme ...                                                                     #")
	for line in config.VITEVITE:

		print('#',end='')

		if (n<0):
			sys.stdout.write(line[-n:])
			for i in range(97-32-n):
				sys.stdout.write(' ')

		elif (n>97-len(line)):
			for i in range(n):
				if (line[0] == "'"):
					sys.stdout.write('-')
				else:
					sys.stdout.write(' ')
			sys.stdout.write(line[:97-n])

		else:
			for i in range(n):
				if (line[0] == "'"):
					sys.stdout.write('-')
				else:
					sys.stdout.write(' ')
			sys.stdout.write(line)
			for i in range(97-32-n):
				sys.stdout.write(' ')

		sys.stdout.write('#\n')
	sys.stdout.flush()
	time.sleep(config.VITEVITE_DELAY)





def display_credits():
	print("#                                                                                                 #")
	print("#                                                                                                 #")
	print("#    Projet réalisé par Baptiste Beltzer et Clément Hoffmann dans le cadre du master CRYPTIS.     #")
	print("#    Chaleureux remerciements à Morgane Vollmer pour l'inspiration artistique.                    #")
	print("#                                                                                                 #")
	print('#                                               ,                                                 #')
	print('#                                              .P.                                                #')
	print('#                                            ,z`  ".                                              #')
	print('#                                   ,,~.   ,^      |                                              #')
	print('#                               "C`     ".,!--~~~-.F                                              #')
	print('#                                 \\  \\~~. `        `\\                                             #')
	print('#                                  L ". `           yQ.                                           #')
	print('#                                  !,              ,ZK$                                           #')
	print("#                                  ,           J$L  **`'2*^\\                                      #")
	print("#                               ,~=4.         "+'"'+"GDF     -HL'/                                      #")
	print('#              -.     ==.    ,^     \\.                 ,J*`                                       #')
	print('#                L    \\.}  ;`        `\\,            /`                                            #')
	print('#                 `=..<^._]              `*~.....~w`                                              #')
	print('#                         |                       /                                               #')
	print('#                         ".                     /L                                               #')
	print('#                           "=              .  )` [                                               #')
	print('#                             .  .,,,  ,,,.*L  L  L                                               #')
	print('#                             .  | |        L  L ..                                               #')
	print('#                             \\.=[ (        !./^``                                                #')
	print("#                                                                                                 #")
	print("#                                                                                                 #")
	print("#                                              (Appuyer sur Entrée pour sortir des crédits)       #")
	print("#                                                                                                 #")
	print("#                                                                                                 #")
	print("#                                                                                                 #")
	input()