# Alarm clock module for yoDo
# ver 1.0.0

import threading, re, datetime, os

class Alarm(threading.Thread):
	def __init__(self, time):
		super(Alarm, self).__init__()
		time = time.split(':')
		self.hours = int(time[0])
		self.minutes = int(time[1])
		self.keep_running = True

	def run(self):
		time = datetime.datetime
		print self.hours
		print self.minutes
		# try:
		while self.keep_running:
			now = time.now()

			if (now.tm_hour == self.hours and now.tm_min == self.minutes):
				print 'ALARM!'
				os.popen("test.mp3")
				return
			time.sleep(30)

		# except:
		# 	print 'DNG'
		# 	return

	def just_die(self):
		self.keep_running = False

def wakeme():
	valid = False
	reg = re.compile('^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$')
	current_time = datetime.datetime.now()
	userbs = raw_input('Time? >> ')

	while valid is False:
		if reg.match(userbs):
			alarm = Alarm(userbs)
			alarm.start()
			valid = True
		else:
			userbs = raw_input('Time? >> ')

wakeme()