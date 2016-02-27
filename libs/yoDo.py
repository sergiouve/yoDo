import os, sys, argparse, json
import importlib as importlib

class Yodo(object):

	def __init__(self, settings = [], userbs = []):
		self.settings = settings
		self.userbs = userbs

	def say_hello(self):
		print 'Hi, my name is yoDo'

	def parse_input(self):
		parser = argparse.ArgumentParser(description='yoDo')
		parser.add_argument('action', nargs = '?', default=None)
		parser.add_argument('opt1', nargs = '?', default = None)
		parser.add_argument('opt2', nargs = '?', default = None)
		parser.add_argument('flags', nargs = '*', default = None)

		args = parser.parse_args()

		return args

	def list_modules(self, options):
		modules = options['settings']['modules']
		print 'Modules available: '

		for module in modules:
			if modules[module]:
				print module

	def exec_mod(self, module, settings, foption = None, soption = None, flags = None, input = []):

		if module == None:
			module = 'whoareyou'

		imported_mod = importlib.import_module(module)
		module_method = getattr(imported_mod, module)
		module_exec = module_method(settings)

	def do(self):
		self.userbs = self.parse_input()

		action = self.userbs.action
		foption = self.userbs.opt1
		soption = self.userbs.opt2
		flags = self.userbs.flags

		self.exec_mod(action, self.settings, foption, soption, flags)