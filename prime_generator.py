#!/usr/bin/python3

import random
import subprocess

def random_prime(max): # max = nombre de chiffres du nombre premier
	p = random_number(max)
	while(not is_prime(p)):
		p = random_number(max)
	return p

def random_number(max): # max = nombre de chiffres du nombre
	nbr = ""
	random.seed()
	for i in range(max - 1, -1, -1):
		if(i == max - 1):
			nbr += random.choice('123456789')
		elif(i == 0):
			nbr += random.choice('1379')
		else:
			nbr += random.choice('0123456789')
	return int(nbr)

def is_prime(p):
	r = subprocess.run("openssl prime " + str(p), shell = True, stdout=subprocess.PIPE)
	if("is prime" in r.stdout.decode("UTF-8")):
		return 1
	return 0

count = 0
for i in range(10000):
	if(is_prime(random_number(100))):
		count += 1
print(count / 10000)