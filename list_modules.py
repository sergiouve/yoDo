# List modules module for yoDo
# ver 1.0.0
import pprint

def list_modules(options):
	modules = options['settings']['modules']
	print 'Modules available: '

	for module in modules:
		if modules[module]:
			print module