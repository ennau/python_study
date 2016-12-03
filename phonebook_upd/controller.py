#from main import create, update, delete, read, show
from main import contacts

flag = ''

c = contacts() # Load main class contacts

# Main logic
while flag != 'exit':
    iselect = str(raw_input("C=Create, R=Read, U=Update, D=Delete, S=Show, exit=exit\n"))

    if iselect == 'R':
        name = raw_input("Search name from dict\n")
        if name in c.phonebook:
            print "{}: phone is {}".format(name, c.phonebook[name])
            c.read(name)
        else:
            print name + ' ' + 'is not found'

    elif iselect == 'C':
        name = raw_input("Create name to dict\n")
        try:
           phone = int(raw_input("Add phone\n"))
        except ValueError:
           print "Phone must be integer!!"
        c.create(name, phone)

    elif iselect == 'U':
        name = raw_input("Search name from dict\n")
        if name in c.phonebook:
            phone = int(raw_input("Update phone\n"))
            print "{}: phone is {}".format(name, phone)
            c.update(name, phone)
        else:
            print name + ' ' + 'is not found'

    elif iselect == 'D':
        name = raw_input("Delete name from dict\n")
        if name in c.phonebook:
            print "Delete {}: phone {}".format(name, phone)
            c.delete(name)
        else:
            print name + ' ' + 'is not found'

    elif iselect == 'S':
        c.show()

    elif iselect == 'exit':
        print 'EXIT program'
        flag = 'exit'

    else:
        print "ERROR, Please choose symbol C U D R S or exit"

else:
    print "Done"
