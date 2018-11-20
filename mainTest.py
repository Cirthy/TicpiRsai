#!/usr/bin/python3

import os, sys, readline, io, select, curses

from  prime_generator  import *
from  rsa              import *
from  display          import *
from  server           import *


import curses, time

def read_char(stdscr):
	"""checking for keypress"""
	stdscr.nodelay(True)  # do not wait for input when calling getch
	return stdscr.getch()

while (True):
	pressed = curses.wrapper(read_char)
	if (pressed != -1):
		print(pressed)
	time.sleep(0.1)


'''
def lecture(stdscr):
	# do not wait for input when calling getch
	stdscr.nodelay(1)
	while True:
		# get keyboard input, returns -1 if none available
		c = stdscr.getch()
		if c != -1:
			# print numeric value
			stdscr.addstr((str(c)+'\n'))
			#stdscr.refresh()
			# return curser to start position
			#stdscr.move(0, 0)



curses.wrapper(lecture)
'''