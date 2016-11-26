serializer = __import__('json')


# Open file phonebook
def wfile():
    try:
        with open('phonebook.txt', 'rt') as gg:
            phonebook = serializer.load(gg)
        print phonebook
    except ValueError:
        phonebook = {'default': 0}
        print phonebook
    return phonebook


# Decorator - save file
def save(phonebook):
    def wrapper():
        res = phonebook()
        with open('phonebook.txt', 'wt') as ff:
            serializer.dump(phonebook, ff)
        return res
    return wrapper
