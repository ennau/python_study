import MySQLdb

# DB phonebook

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root",
                     db="phonebook"
                     )

cur = db.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS phonebook ("
    "id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
    "name VARCHAR(30) NOT NULL UNIQUE, "
    "phone INT);"
    )

# Decorator - save file
def save_dec(f):
    def wrapper():
        db.commit()
        res = f()
        return res
    return wrapper


@save_dec
def create():
    name = raw_input("Create name to dict\n")
    phone = int(raw_input("Add phone\n"))
    try:
        cur.execute("INSERT INTO phonebook (name, phone) VALUES ('{}', {})".format(name, phone))
        cur.execute("SELECT id,name,phone FROM phonebook WHERE name='{}'".format(name))
        for row in cur:
            print row
    except:
        print "SQL CREATE ERROR"

@save_dec
def update():
    name = raw_input("Search name from dict\n")
    phone = int(raw_input("Update phone\n"))
    try:
        cur.execute("UPDATE phonebook SET phone={} WHERE name='{}'".format(phone, name))
        cur.execute("SELECT id,name,phone FROM phonebook WHERE name='{}'".format(name))
        for row in cur:
            print row
    except:
        print "SQL UPDATE ERROR"

@save_dec
def delete():
    name = raw_input("Delete name from dict\n")
    try:
        cur.execute("DELETE FROM phonebook WHERE name='{}'".format(name))
    except:
        print "SQL DELETE ERROR"


def read():
    name = raw_input("Search name from dict\n")
    try:
        cur.execute("SELECT id,name,phone FROM phonebook WHERE name='{}'".format(name))
        for row in cur:
            print row

    except:
        print "SQL SELECT ERROR"


def show():
    try:
        cur.execute("SELECT * FROM phonebook LIMIT 10")
        for row in cur:
            print row
    except:
        print "SQL ERROR"


def quit():
    db.close()


