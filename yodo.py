#!/usr/bin/env python
#YODO 0.0.1

# # # # # # # # # # # # # # # # # # # # #
#	TODO
#	-? Import modules according to what is needed
#	-! Add regex controll to wakeme
#
# # # # # # # # # # # # # # # # # # # # #

import os, sys, argparse, json
from wakeme import *
from setup_yodo import *
from list_modules import *

dev = True
current_dir = os.getcwd()
ver = '0.0.1'

if dev:
	import pprint
	print '--------------'
	print 'Dev stuff, nevermind...'
	print 'yoDo ver: \t\t' + ver
	print 'Sys: \t\t' + sys.platform
	sys.stdout.write('Args: \t\t')
	for arg in sys.argv:
		sys.stdout.write(arg)
	print
	print '--------------'

def load_settings():
	global options

	if os.path.isfile('settings'):
		opts_file = open('settings', 'r')
		opts_str = opts_file.read()
		options = json.loads(opts_str)
		# pprint.pprint(options)
	else:
		setup_yodo()

def main():
	load_settings()
	parser = argparse.ArgumentParser(description='yoDo')
	parser.add_argument('action', nargs = '?', default=None)
	parser.add_argument('opt1', nargs = '?', default = None)
	parser.add_argument('opt2', nargs = '?', default = None)
	parser.add_argument('flags', nargs = '*', default = None)

	args = parser.parse_args()
	action = args.action
	foption = args.opt1
	soption = args.opt2
	flags = args.flags

	if action == 'wakeme':
		wakeme()
	elif action == 'list':
		list_modules(options)
	else:
		print 'My name is yoDo'

if __name__ == '__main__':
	main()