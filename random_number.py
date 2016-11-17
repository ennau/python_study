# coding utf-8
import random

secret = random.randint(1, 10)

counter = 0

while counter < 5:
        try:
                guess = int(raw_input("?\n"))
        except ValueError:
                print "please enter number"
                continue
        counter += 1
        if secret == guess:
                print "WELL DONE!"
                break
        if secret > guess:
                print ">"
        else:
                print "<"
else:
        print "You are looser"

