from main import create, update, delete, read, show

flag = ''

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
