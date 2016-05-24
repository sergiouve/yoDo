import sys
import os
import json
import subprocess

def fishhke(settings):

	action = settings['foption']
	soption = settings['soption']

	if not action:
		action = 'test'

	if action == 'init':
		print 'WUBBA LUBBA INIT'
		options = settings['settings']['modules']['fishhke']

		use_templates = options['templates']
		dirTree = options['directories']

		for folder in dirTree:
			if dirTree[folder] and not (os.path.isdir(folder)):
				os.mkdir(folder)

	elif action == 'new':
		
		create_fishh_project(project_name)
	else:
		print 'What would you like to do? (init/new)'

def is_fishh_project():
	is_fishh = False
	current_path = os.getcwd()

	if os.path.isdir(current_path + '/fishh'):
		is_fishh = True

	return is_fishh

def create_fishh_project(project_name = 'my-new-fishh.com'):
	fishh_repo = 'https://bitbucket.org/t4xi/fishh-clean'
	cmd = 'mkdir ' + project_name + ' && git clone ' + fishh_repo + ' ' + project_name
	subprocess.Popen(cmd, shell = True)
