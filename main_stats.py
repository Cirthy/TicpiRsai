#!/usr/bin/python3

import	os, sys, readline, io, select, curses, random, config

from	prime_generator	import *
from	rsa				import *
from	display			import *
from	network			import *

def random_prime_1(size): # size = nombre de chiffres du nombre premier
	p = random_number(size)
	while(not is_prime(p)):
		p = random_number(size)
	return p

def random_prime_2(size): # size = nombre de chiffres du nombre premier
	p = random_number(size)
	while(not is_prime(p)):
		p -= 2
	return p





NOMBRE = 10
PRIME_SIZE_TEST = 50
ALGO = "shuffle"
#ALGO = "-=2"

print("Génération de {0} nombres premiers à {1} chiffres par l'algo {2}.".format(NOMBRE,PRIME_SIZE_TEST,ALGO))
for i in range(NOMBRE):
	print("\r{0:5}".format(i), end ='')
	if (ALGO == "shuffle"):
		random_prime_1(PRIME_SIZE_TEST)
	if (ALGO == "-=2"):
		random_prime_2(PRIME_SIZE_TEST)

