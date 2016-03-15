from sys import platform as _platform
import subprocess
import psutil

def getmydaygoin(settings):

	what_you_need = settings['settings']['modules']['getmydaygoin']['software']

	for proc in psutil.process_iter():
		if proc.name() in what_you_need:
			what_you_need.remove(proc.name())

	for software in what_you_need:
		if _platform == 'linux' or _platform == 'linux2' or _platform == 'darwin':
			cmd = 'nohup ' + software + ' </dev/null >/dev/null 2>&1 &'
			subprocess.Popen(cmd, shell = True)
			cmd = None
		else:
			print 'Not quite yet implemented...'