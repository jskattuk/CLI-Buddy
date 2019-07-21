![alt-text](https://github.com/jskattuk/CLI-Buddy/blob/master/CLI_Buddy_Window.PNG)

# CLI-Buddy

CLI-Buddy is an application that allows you to search for command line commands. Simply enter some keywords into the box and click the arrow button (or hit <kbd>Enter</kbd>) and the application will return a list of all commands in the MongoDB database that contain at least one of the words. 

Leaving the box empty will return all of the commands stored in the database. If you wish to exactly match multiple words, encase everything in double/single quotes, and the application will look for an exact match of the string you have input. Note that you cannot mix and match both quoted and non-quoted keywords in the same search. Clicking on a command from the list will open up its man page on the command line, where you can read up on further information.
            
Disclaimer: This is by no means a comprehensive list of command line commands, and it only contains the commands in section 1 of the man pages. Hope you find this tool useful!

You can read all of this information by clicking on the "Info About CLI-Buddy" button within the application.

# How to run CLI-Buddy

In order to run this application properly:

1. You must specify your own MongoDB instance in both CLIBuddy.py and PopulateDB.py, in the places indicated. This can be done by inserting a MongoDB Connection String URI.

2. You must run PopulateDB.py before running CLIBuddy.py, so that a database may be created and populated with commands. You will only ever need to run PopulateDB.py once, as once the database is created it will persist, and CLI-Buddy can be run as many times as you like.
