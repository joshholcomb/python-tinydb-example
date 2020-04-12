from tinydb import TinyDB, Query
import sys
import argparse
import json


#
# function to retrieve input from user
#
def getUserInput():
    name = input("enter name: ") 
    age = int(input("enter age: "))
    return(name, age)


def main(argv):
    # setup command line arguments
    argParser = argparse.ArgumentParser()
    argParser.add_argument("--insert", action="store_true")
    argParser.add_argument("--print", action="store_true")
    argParser.add_argument("--purgedb", action="store_true")
    argParser.add_argument("--searchname")
    argParser.add_argument("--searchage", type=int)

    args = argParser.parse_args()

    # init db
    db = TinyDB('db.json')
    people = db.table('people')

    if (args.insert):    
        # insert new person
        (name, age) = getUserInput()
        people.insert({'name': name, 'age': age})

    if (args.print):
        # print the contents of the people table
        dbSize = len(people)
        print ("table has [{}] values".format(dbSize))
        i = 0
        for r in people:
            i = i + 1
            name = r.get('name')
            age = r.get('age')
            print ("{} - name: [{}] | age: [{}]".format(i, name, age))
        
    if (args.purgedb):
        # purge database
        print("purging database...")
        db.purge_table('people')

    if (args.searchname):
        # search db for value
        Person = Query()
        res = people.search(Person.name == args.searchname)
        i = 0
        for r in res:
            i = i + 1
            name = r.get('name')
            age = r.get('age')
            print ("{} - name: [{}] | age: [{}]".format(i, name, age))

    if (args.searchage):
        # search db for people of given age
        Person = Query()
        res = people.search(Person.age == args.searchage)
        i = 0
        for r in res:
            i = i + 1
            name = r.get('name')
            age = r.get('age')
            print ("{} - name: [{}] | age: [{}]".format(i, name, age))


if __name__ == "__main__":
    main(sys.argv[1:])