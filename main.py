#!/usr/bin/python3

import os
from prime_generator import *
from rsa import *
from display import *

#pid = os.fork()
#if(not pid):
#	display_waiting(pid)
p, q = random_prime(config.primeSize), random_prime(config.primeSize)
#os.kill(pid, 15)
cypher = encrypt("Coucou", p * q)
print(str(cypher) + "\n\n___________________\n")
plain = decrypt(cypher, p, q)
print(plain)