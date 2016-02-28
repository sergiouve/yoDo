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

		first_run = True

		if first_run:

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
			print settingsAr

		else:
			clear()
			print 'Not the first time uh?'


	else:
		clear()
		print text['welcome_not_new']

def read_modules():
	"""read_modules"""