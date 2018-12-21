#!/usr/bin/python3

import	config
import	binascii



def encrypt(plain):
	encodedPlain = int(binascii.hexlify(plain.encode('utf-8')), 16)
	return lpowmod(encodedPlain, config.e, config.n_distant)


def decrypt(cipher):
	encodedPlain = lpowmod(cipher, config.d, config.n_local)
	return binascii.unhexlify(hex(encodedPlain)[2:].encode('ascii')).decode('utf-8')


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
