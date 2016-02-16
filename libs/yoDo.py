import os, sys, argparse, json

class Yodo(object):

	def __init__(self, options = [], userbs = []):
		self.options = options
		self.userbs = userbs

	def say_hello(self):
		print 'Hi, my name is yoDo'

	def load_settings(self, settings_file):
		with open(settings_file) as settings_file:
			options = json.load(settings_file)

		return options

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

	def load_modules(self, module = None):

		if(module is None):
			module = 'whoareyou'

		__import__(module)

	def do(self):

		self.load_settings('settings')
		self.userbs = self.parse_input()

		action = self.userbs.action
		foption = self.userbs.opt1
		soption = self.userbs.opt2
		flags = self.userbs.flags

		self.load_modules(action)