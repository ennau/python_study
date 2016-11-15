# python_study
# coding utf-8
import random

secret = random.randint(1, 10) 
while True:
	try:
		guess = int(raw_input("?"))
	except ValueError:
		print "please enter number"		
		continue
	if secret == guess:
		print "WELL DONE!"
		break
	if secret > guess:
		print ">"
	else:
		print "<"

