import subprocess
import psutil

def getmydaygoin():

	what_you_need = ['spotify', 'atom', 'firefox']

	for proc in psutil.process_iter():
		if proc.name() in what_you_need:
			what_you_need.remove(proc.name())

	for software in what_you_need:
		background_run = subprocess.Popen(subprocess.call(['nohup', software, '&']))

getmydaygoin()