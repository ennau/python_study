#from lsfile import save_dec, wfile

import ConfigParser

# Use config.py
config = ConfigParser.ConfigParser()
config.read('config.py')
filetype = config.get('Main', 'format')

if filetype == 'csv':
    from lsfile_csv import save, wfile
elif filetype == 'json':
    from lsfile import save, wfile
else:
    print "Unsupported format"



phonebook = wfile()
phone = ''


# Decorator - save file
def save_dec(f):
    def wrapper():
        res = f()
        save(phonebook)
        return res
    return wrapper


@save_dec
def create():
    name = raw_input("Create name to dict\n")
    try:
        phone = int(raw_input("Add phone\n"))
        phonebook[name] = phone
        # print phonebook
    except ValueError:
        print "Phone must be integer!!"


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
def delete():
    name = raw_input("Delete name from dict\n")
    if name in phonebook:
        del phonebook[name]
        print "Delete {}: phone {}".format(name, phone)
    else:
        print name + ' ' + 'is not found'


def read():
    name = raw_input("Search name from dict\n")
    if name in phonebook:
        print "{}: phone is {}".format(name, phonebook[name])
    else:
        print name + ' ' + 'is not found'


def show():
    print phonebook
