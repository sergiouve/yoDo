import os, sys, argparse, json

class Yodo(object):

	def __init__(self, options = [], user_bs = []):
		self.options = options
		self.user_bs = user_bs

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
		self.user_bs = self.parse_input()

		action = self.user_bs.action
		foption = self.user_bs.opt1
		soption = self.user_bs.opt2
		flags = self.user_bs.flags

		self.load_modules(action)