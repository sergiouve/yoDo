# Alarm clock module for yoDo
# ver 1.0.0

import threading, re, datetime
from pygame import mixer

def wakeme():
	valid = False
	reg = re.compile('^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$')
	current_time = datetime.datetime.now()
	userbs = raw_input('At what time? >> ')

	while valid is False:
		if userbs:
			if reg.match(userbs):

				valid = True
			else:
				userbs = raw_input('At what time? >> ')
		else:
			userbs = raw_input('At what time? >> ')