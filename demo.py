# demo.py

import subprocess

def insecure(): 
	cmd = input("Enter command: ")
	subprocess.call(cmd, shell=True)

insecure()
