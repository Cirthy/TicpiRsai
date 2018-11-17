#!/usr/bin/python3

import config

def encrypt(plain, n):
	encodedPlain = ''
	for i in (plain.encode('UTF-8')):
		encodedPlain += str(hex(i))[2:]
	print(str(int(encodedPlain, 16)) + "\n\n")
	return lpowmod(int(encodedPlain, 16), config.e, n)

def decrypt(cipher, p, q):
	d = modinv(config.e, (p - 1) * (q - 1))
	return lpowmod(cipher, d, p * q)

def ecgd(a, b):
	x, y, u, v = 0, 1, 1, 0
	while(a != 0):
		q, r = b // a, b % a
		m, n = x - u * q, y - v * q
		b, a, x, y, u, v = a, r, u, v, m, n
	gcd = b
	return gcd, x, y

def modinv(a, m): # renvoie l'inverse de a modulo m
	gcd, x, y = ecgd(a, m)
	if(gcd != 1):
		return None
	return x % m

def lpowmod(x, y, n): #renvoie (x**y)%n ; x, y, n entiers
	result = 1
	while(y > 0):
		if(y&1 > 0):
			result = (result * x) % n
		y >>= 1
		x = (x * x) % n
	return result
