import os
import re

clear = lambda: os.system('clear')
text = {
	'welcome_new': 'Welcome to the yodo whatever, now you\'ll be asked some questions',
	'welcome_raw': 'let\'s get started >> ',
	'name_question_raw': 'What\'s your name? (You can leave this blank, and I\'ll just give you a random name) >> ',
	'email_question_raw': 'What\'s your email? (You can leave this blank) >> ',
	'email_question_error': 'Oh, c\'mon you can do this, insert a valid email, ',
	'goodbye': 'Everything seems to be OK. Off you go!',
	'welcome_not_new': 'Hi, there '
}

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def setsettings(settings):

	global user_settings
	global modules_settings

	user_settings = settings['settings']['user']
	modules_settings = settings['settings']['modules']

	if not os.path.isfile('settings'):

		first_run = False

		if first_run:
			clear()
			showmenu()

		else:
			clear()
			show_menu()


	else:
		clear()
		show_menu()


def read_modules():
	print settings
	"""modules ="""


def start_settings():
	settingsAr = {}
	userInfo = {}
	clear()
	print text['welcome_new']
	userInfo['name'] = raw_input(text['name_question_raw'])
	clear()
	if userInfo['name'] == '':
		userInfo['name'] = 'Pisshead'

	userInfo['email'] = raw_input(text['email_question_raw'])
	clear()
	if userInfo['email'] != '':
		while not EMAIL_REGEX.match(userInfo['email']) or userInfo['mail'] == '':
			print text['email_question_error'] + userInfo['name']
			userInfo['email'] = raw_input(text['name_question_raw'])
			clear()

	settingsAr['user_info'] = userInfo


def show_menu():

	show_header()

	print 	'''
 YODO CONF SCRIPT
 What would you like to tweak?

 1. yodo Core
			'''

	n_option = 2
	options = []
	index = 0

	for key, value in modules_settings.iteritems():
		if not isinstance(value, bool):
			print ' ' + str(n_option) + '. ' + key
			options.insert(index, value)
			n_option += 1
			index += 1

	print''
	print ' 0. Exit'
	print''

	userbs = int(raw_input(' Choose an option >> '))
	n_option -= 1

	while userbs < 0 or userbs > n_option:
		userbs = int(raw_input(' Choose an option >> '))

	if userbs == 0:
		clear()
		print 'G\'bye!'
		exit()

	elif userbs == 1:
		show_core_options()

	else:
		options_ar_index = userbs - 2
		print options_ar_index
		# print options
		# show_module_options(options[options_ar_index])


def show_core_options():
	show_header()
	print 'yodo Core configuration'
	userbs = raw_input( 'Continue? >> ')

	while userbs is not 'y':
		userbs = raw_input( 'Continue? >> ')

	show_menu()

def show_module_options(module_id):
	show_header()
	print modules_settings[module_id]
	# print 'yodo ' + modules_settings[module_id] + ' configuration'
	userbs = raw_input( 'Continue? >> ')

	while userbs is not 'y':
		userbs = raw_input( 'Continue? >> ')

	show_menu()

def show_header():
	clear()
	print '''
# # # # # # # # # # # # # # # # #
#    __  ______  ___  ____      #
#    \ \/ / __ \/ _ \/ __ \\     #
#     \  / /_/ / // / /_/ /     #
#     /_/\____/____/\____/      #
#                               #
# # # # # # # # # # # # # # # # #
                                ver 0.1.0
			'''