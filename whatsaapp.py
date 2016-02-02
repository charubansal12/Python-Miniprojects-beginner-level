import webbrowser
import os
import signal
import tkMessageBox
from subprocess import check_output


def get_pid(name):
	return int(check_output(["pidof","-s",name]))
'''Script to open whatsapp web whenever chrome is opened'''

name="chrome"
if (get_pid(name)):
	webbrowser.open('http://web.whatsapp.com')
	tkMessageBox.showinfo(title="Greetings", message="Connect your phone to chrome to open whatsapp!")
