#!/usr/bin/python3

import os
from prime_generator import *
from rsa import *
from display import *

p, q = random_prime(config.primeSize), random_prime(config.primeSize)
cypher = encrypt(input("Enter message : "), p * q)
plain = decrypt(cypher, p, q)
print("\n\n" + plain)