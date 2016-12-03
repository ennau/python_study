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



# Decorator - save file
def save_dec(f):
    def wrapper(self):
        res = f()
        save(self.phonebook)
        return res
    return wrapper


class contacts(object):
    def __init__(self):
        self.phonebook = wfile()
        self.phone = ''

    '''
    Business logic
    '''

    def create(self, name, phone):
        self.phonebook[name] = phone

    def update(self, name, phone):
        self.phonebook[name] = phone



    def delete(self):
        name = raw_input("Delete name from dict\n")
        if name in self.phonebook:
            del self.phonebook[name]
            print "Delete {}: phone {}".format(name, self.phone)
        else:
            print name + ' ' + 'is not found'


    def read(self):
        name = raw_input("Search name from dict\n")
        if name in self.phonebook:
            print "{}: phone is {}".format(name, self.phonebook[name])
        else:
            print name + ' ' + 'is not found'


    def show(self):
        print self.phonebook
