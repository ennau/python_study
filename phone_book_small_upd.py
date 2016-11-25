 coding utf-8

#phonebook['BILL'] = 911
#phonebook['BOB'] = 912
#print '\n'.join(["{}: {}".format(name, phone) for name, phone in d.items()])

phonebook = {}
flag = ''
command = []
phone = ''

def read():
    name = raw_input("Search name from dict\n")
    if name in phonebook:
        print "{}: phone is {}".format(name, phone)
    else:
        print name + ' ' + 'is not found'

def delete():
    name = raw_input("Delete name from dict\n")
    if name in phonebook:
        del phonebook[name]
        print "Delete {}: phone {}".format(name, phone)
    else:
        print name + ' ' + 'is not found'

def update():
    name = raw_input("Search name from dict\n")
    phone = int(raw_input("Update phone\n"))
    if name in phonebook:
        phonebook[name] = phone
        print "{}: phone is {}".format(name, phone)
    else:
        print name + ' ' + 'is not found'

def create():
    name = raw_input("Create name to dict\n")
    phone = int(raw_input("Add phone\n"))
    phonebook[name] = phone

while flag != 'exit':
    iselect = str(raw_input("C=Create, R=Read, U=Update, D=Delete, exit=exit\n"))

    if iselect == 'R':
        read()

    elif iselect == 'C':
        create()

    elif iselect == 'U':
        update()

    elif iselect == 'D':
        delete()

    elif iselect == 'exit':
        print 'EXIT'
        flag = 'exit'
    else:
        print "ERROR, Please choose C U D R or exit"
else:
    print "Exit!"
