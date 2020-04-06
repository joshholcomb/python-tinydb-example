from tinydb import TinyDB, Query
import sys
import argparse
import json

def getUserInput():
    # get name from user input
    name = input("enter name: ") 
    # get age from user input
    age = int(input("enter age: "))

    return(name, age)

def main(argv):

    # command line arguments
    argParser = argparse.ArgumentParser()
    argParser.add_argument("--insert", action="store_true")
    argParser.add_argument("--print", action="store_true")
    argParser.add_argument("--purgedb", action="store_true")
    args = argParser.parse_args()

    # init db
    db = TinyDB('db.json')
    people = db.table('people')

    if (args.insert):    
        # insert new person
        (name, age) = getUserInput()
        people.insert({'name': name, 'age': age})

    if (args.print):
        # print table contents
        dbSize = len(people)
        print ("table has [{}] values".format(dbSize))
        i = 0
        for r in people:
            i = i + 1
            name = r.get('name')
            age = r.get('age')
            print ("{} - name: [{}] | age: [{}]".format(i, name, age))
        
    if (args.purgedb):
        print("purging database...")
        db.purge_table('people')


if __name__ == "__main__":
    main(sys.argv[1:])