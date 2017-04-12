import os


def listmods(settings):

  modules_folder = settings['paths']['modules']

  for module in os.listdir(modules_folder):
    if module.endswith('.py') and module != '__init__.py':
      module = module.replace('.py', '')
      print(module)
