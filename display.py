#!/usr/bin/python3

import time
import sys
import os

def display_waiting(p):
	pid = os.fork()
	if(not pid):
		while(1):
			sys.stdout.write('\b\b\b.  ' + str(pid))
			sys.stdout.flush()
			time.sleep(0.7)
			sys.stdout.write('\b\b\b.. ')
			sys.stdout.flush()
			time.sleep(0.7)
			sys.stdout.write('\b\b\b...')
			sys.stdout.flush()
			time.sleep(0.7)
	time.sleep(10)
	os.kill(pid, 15)

def remove_display_waiting():
	sys.stdout.flush()
	sys.stdout.write('\b\b\b')