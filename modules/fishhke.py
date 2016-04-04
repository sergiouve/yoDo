import sys
import os
import git
import json

def fishhke(settings):

	if action == 'init':
		print 'WUBBA LUBBA INIT'
		options = setting['modules']['fishhke']

		else:
			main_menu()

		use_templates = options['templates']
		dirTree = options['directories']

		for folder in dirTree:
			if dirTree[folder] and not (os.path.isdir(folder)):
				os.mkdir(folder)

	elif action == 'create':
		print 'WUBBA LUBBA GENERATE'

	else:
		print 'WUBBA LUBBA ERROR!'

def is_fishh_project():
	is_fishh = False
	current_path = os.getcwd()

	if os.path.isdir(current_path + '/fishh'):
		is_fishh = True

	return is_fishh

def create_fishh_project():
	fishh_repo = 'https://bitbucket.org/t4xi/fishh-clean'
	git.Git().clone(fishh_repo)
