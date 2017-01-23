import os, sys, argparse, json
import importlib as importlib
import pprint

class Yodo(object):

    def __init__(self, settings = [], user_input = []):
        self.settings = settings
        self.user_input = user_input

    def parse_input(self):
        parser = argparse.ArgumentParser(description='yoDo')
        parser.add_argument('action', nargs = '?', default=None)
        parser.add_argument('opt1', nargs = '?', default = None)
        parser.add_argument('opt2', nargs = '?', default = None)
        parser.add_argument('flags', nargs = '*', default = None)

        args = parser.parse_args()

        return args

    def exec_mod(self, module, settings, foption = None, soption = None, flags = None, input = []):

        if module == None:
        	module = 'whoareyou'

        try:
        	imported_mod = importlib.import_module(module)
        except ImportError as exc:
        	print module + ' doesn\'t seems to be a yodo module...'
        	sys.stderr.write("Error: failed to import settings module ({})".format(exc))
        	sys.exit(1)

        module_method = getattr(imported_mod, module)

        settings['foption'] = foption
        settings['soption'] = soption
        settings['flags'] = flags

        module_exec = module_method(settings)

    def do(self):
        self.user_input = self.parse_input()

        action = self.user_input.action
        foption = self.user_input.opt1
        soption = self.user_input.opt2
        flags = self.user_input.flags

        self.exec_mod(action, self.settings, foption, soption, flags)
