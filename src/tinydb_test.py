from tinydb import TinyDB, Query

def getUserInput():
    # get name from user input
    name = input("enter name: ") 
    # get age from user input
    age = int(input("enter age: "))

    return(name, age)


(name, age) = getUserInput()

db = TinyDB('db.json')
people = db.table('people')
people.insert({'name': name, 'age': age})

print("table contents")
print(people.all())