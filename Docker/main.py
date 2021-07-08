#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print()

f=cgi.FieldStorage()
cmd=f.getvalue("x")

if cmd.startswith("docker") == True:
	o = subprocess.getoutput("sudo " + cmd)
	print(o)
else:
	print("Not a docker command, please enter the valid docker command")
 

