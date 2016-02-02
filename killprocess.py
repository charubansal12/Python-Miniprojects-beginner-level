#Kill process in python
import os 
import signal
from subprocess import check_output

def get_pid(name):
	return int(check_output(["pidof","-s",name]))

'''print "List of currently running processes are :"
pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

for pid in pids :
	try:
		print open(os.path.join('/proc',pid,'cmdline'),'rb').read()
	except IOError:		#proc has already terminated
		continue
'''		
name = raw_input("Enter the name of process to kill")

id1= get_pid(name)
#print id1
os.kill(id1,signal.SIGTERM)
