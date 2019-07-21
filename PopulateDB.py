# this code will create a database in a given MongoDB instance and populate it with 
# the commands specified in the command_list.txt file
from pymongo import MongoClient

# establish connection to MongoDB instance (NOTE: you will need to specify your own instance)
client = MongoClient("<<Insert Connection URI here>>")
db = client.command_db

lines = open("CLI-Buddy/command_list.txt", "r")
for line in lines:
    words = line.split(" ")
    name = words[0]
    desc = (" ").join(words[(words.index("-") + 1):])
    entry = "{}: {}".format(name, desc)
    entry = entry.strip('\n')
    db_entry = {
        "command" : entry
    }
    result = db.commands.insert_one(db_entry)
