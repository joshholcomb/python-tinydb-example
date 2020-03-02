from tinydb import TinyDB, Query
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

db = TinyDB('dbperf.json')
table = db.table('count')

rows = 1000
row = 0
while (row < rows):
    row = row + 1
    name = randomString(5)
    print("inserting row [{}] - name: [{}]".format(row, name))
    table.insert({'count': row, 'name': name})