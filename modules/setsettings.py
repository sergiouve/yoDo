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
	if not os.path.isfile('_settings'):

		first_run = False

		if first_run:

			clear()
			showmenu()

		else:
			clear()
			show_menu()


	else:
		clear()
		print text['welcome_not_new']


def read_modules():
	"""read_modules???"""


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

	print '''
 YODO CONF SCRIPT
 What would you like to do?

 1. Packages
 2. APIS
 3. GUI
 4. Do not enter

 0. Exit
			'''
	userbs = int(raw_input(' Choose an option >> '))
	while userbs < 0 or userbs > 4:
		userbs = int(raw_input(' Choose an option >> '))

	print userbs

	if userbs == 0:
		print 'G\'bye!'
		exit()

	if userbs == 1:
		show_opt1()

	if userbs == 2:
		show_opt2()

	if userbs == 3:
		show_opt3()

	if userbs == 4:
		show_opt4()


def show_opt1():
	print 'Opt 1'
	show_menu()

def show_opt2():
	print 'Opt 2'
	show_menu()

def show_opt3():
	print 'Opt 3'
	show_menu()

def show_opt4():
	print 'Opt 4'
	show_menu()

def show_header():
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