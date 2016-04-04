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

	'''check for fishh project structure'''

	return is_fishh

def create_fishh_project():
	fishh_repo = 'https://bitbucket.org/t4xi/fishh-clean'
	git.Git().clone(fishh_repo)