serializer = __import__('csv')

# Open file phonebook
def wfile():
    try:
        with open('phonebook.csv', 'rt') as csvfile:
            phonebook = serializer.reader(csvfile, delimiter=' ', quotechar='|')
            phr = dict([row for row in phonebook])
        print phonebook
    except ValueError:
        phr = {'default': 0}
        print phr
    return phr

def save(phonebook):
    with open('phonebook.csv', 'wt') as ff:
            w = serializer.writer(ff, delimiter=' ',
                            quotechar='|', quoting=serializer.QUOTE_MINIMAL)
            for row in phonebook.items():
                w.writerow(row)
                
