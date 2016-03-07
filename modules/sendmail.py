import os

clear = lambda: os.system('clear')

def sendmail(settings):
	mail_client = settings['settings']['modules']['sendmail']['mail_client']
	contacts = settings['settings']['modules']['sendmail']['contacts']
	body = settings['settings']['modules']['sendmail']['mail_bodies']['regular_call']

	contact_names = contacts.keys()
	contact_emails = contacts.values()
	clear()
	caller = raw_input('Who called? >> ')
	company = raw_input('Which company? >> ')

	print 'Who did they asked for?'

	n = 1
	for name in contact_names:
		print str(n) + '. ' + name
		n += 1

	wanted_id = -1
	n -= 1

	while wanted_id < 0 or wanted_id > n:
		wanted_id = input('>> ')

	wanted_id -= 1
	print wanted_id

	mail_to = contact_emails[wanted_id]
	name_to = contact_names[wanted_id]

	body = body.replace('$name', name_to)
	body = body.replace('$caller', caller)
	body = body.replace('$company', company)

	if mail_client == 'thunderbird':
		cmd = mail_client +  " -compose to='" + mail_to + "',subject='" + caller + " - " + company +  "',body='" + body + "'"
		os.system(cmd)
	else:
		print 'Not quite implemented yet mate...'