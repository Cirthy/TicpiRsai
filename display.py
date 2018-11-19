#!/usr/bin/python3

import time
import sys
import os
import config


def display_menu():
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
	display_menu()
	print("# Chargement du programme ...                                                                     #")
	for line in config.VITEVITE:
		
		print('#',end='')

		if (n<0):
			print(line[-n:],end='')
			for i in range(97-32-n):
				print(' ',end='')

		elif (n>97-len(line)):
			for i in range(n):
				if (line[0] == "'"):
					print('-',end='')
				else:
					print(' ',end='')
			print(line[:97-n],end='')

		else:
			for i in range(n):
				if (line[0] == "'"):
					print('-',end='')
				else:
					print(' ',end='')
			print(line,end='')
			for i in range(97-32-n):
				print(' ',end='')
		print('#')
	sys.stdout.flush()
	time.sleep(config.VITEVITE_DELAY)







def display_waiting():
	i=0
	while(1):
		dispay_progress_bar(i%(config.PROGRESS_BAR_SIZE+2)-2)
		i+=1

def dislpay_progress_bar(n):
	compt = 0
	ntemp = n
	sys.stdout.write('|')
	for i in range(max(n,0)):
		sys.stdout.write(' ')
	while(ntemp>=-2 and compt<3 and ntemp<config.PROGRESS_BAR_SIZE):
		sys.stdout.write('-')
		compt+=1
		if (ntemp<0):
			ntemp-=1
		elif (ntemp>=config.PROGRESS_BAR_SIZE-2):
			ntemp+=1
	for i in range(max(config.PROGRESS_BAR_SIZE-max(n,0)-compt,0)):
		sys.stdout.write(' ')
	sys.stdout.write('|')
	sys.stdout.flush()
	time.sleep(0.2)
	for i in range(config.PROGRESS_BAR_SIZE+2):
		sys.stdout.write('\b')



def remove_display_waiting():
	sys.stdout.flush()
	sys.stdout.write('\b\b\b')



