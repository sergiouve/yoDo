class Yodo(object):

	from wakeme import *
	from setup_yodo import *
	from list_modules import *

	def say_hello(self):
		print 'Hi, my name is yoDo'

	def import_modules(self):
		print 'import_modules()'

	def parse_input(self):
		

	# List modules module for yoDo
	# ver 1.0.0
	import pprint

	def list_modules(options):
		modules = options['settings']['modules']
		print 'Modules available: '

		for module in modules:
			if modules[module]:
				print module