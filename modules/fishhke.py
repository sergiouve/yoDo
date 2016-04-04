import sys
import os
import git

def fishhke(settings):

	if is_fishh_project():
		print 'scafold!'
	else:
		create_fishh_project()

def is_fishh_project():
	is_fishh = False
	current_path = os.getcwd()

	if os.path.isdir(current_path + '/fishh'):
		is_fishh = True

	return is_fishh

def create_fishh_project():
	fishh_repo = 'https://bitbucket.org/t4xi/fishh-clean'
	git.Git().clone(fishh_repo)