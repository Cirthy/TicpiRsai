#!/usr/bin/python3

import os
from prime_generator import *
from rsa import *
from display import *





pid = os.fork()

if not pid :
	display_waiting_vitevite()

p, q = random_prime(config.primeSize), random_prime(config.primeSize)
os.kill(pid, 9)



display_menu()
print('\n\n')

print(p)
print(q)



cypher = encrypt(input("Enter message : "), p * q)
plain = decrypt(cypher, p, q)
print("cypher = " + str(cypher) + "\nplain : " + plain)