# coding utf-8

import json

#phonebook['BILL'] = 911
#phonebook['BOB'] = 912
#print '\n'.join(["{}: {}".format(name, phone) for name, phone in d.items()])

"""
#### EDIT!!!

def f_a():
...     print 'Func a'
...
def f_b():
..     print 'Func b'
...
def f_c():
...     print 'Func c'
action = raw_input('?')
?b
d = {'a': f_a, 'b': f_b, 'c': f_c}
d[action]()
Func b
def default():
...     print 'Default'
...
d.get(action, default)()
Func b
action = 'x'
d.get(action, default)()
Default
type(d)
<type 'dict'>
"""


phonebook = {}
flag = ''
command = []
phone = ''

# Open file phonebook
try:
    with open('phonebook.txt', 'rt') as gg:
        phonebook = json.load(gg)
    print phonebook
except ValueError:
    phonebook={'default': 0}
    print phonebook

# Decorator - save file
def save_dec(f):
    def wrapper():
        res = f()
        with open ('phonebook.txt', 'wt') as ff:
            json.dump(phonebook, ff)
        return res
    return wrapper

# Main functions
def read():
    name = raw_input("Search name from dict\n")
    if name in phonebook:
        print "{}: phone is {}".format(name, phonebook[name])
    else:
        print name + ' ' + 'is not found'

@save_dec
def delete():
    name = raw_input("Delete name from dict\n")
    if name in phonebook:
        del phonebook[name]
        print "Delete {}: phone {}".format(name, phone)
    else:
        print name + ' ' + 'is not found'

@save_dec
def update():
    name = raw_input("Search name from dict\n")
    phone = int(raw_input("Update phone\n"))
    if name in phonebook:
        phonebook[name] = phone
        print "{}: phone is {}".format(name, phone)
    else:
        print name + ' ' + 'is not found'

@save_dec
def create():
    name = raw_input("Create name to dict\n")
    phone = int(raw_input("Add phone\n"))
    phonebook[name] = phone
    print phonebook

def show():
    print phonebook

# Main logic
while flag != 'exit':
    iselect = str(raw_input("C=Create, R=Read, U=Update, D=Delete, S=Show, exit=exit\n"))

    if iselect == 'R':
        read()
    elif iselect == 'C':
        create()
    elif iselect == 'U':
        update()
    elif iselect == 'D':
        delete()
    elif iselect == 'S':
        show()
    elif iselect == 'exit':
        print 'EXIT program'
        flag = 'exit'
    else:
        print "ERROR, Please choose symbol C U D R S or exit"
else:
    print "Done"

