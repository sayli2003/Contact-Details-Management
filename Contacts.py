# here we must write the code to file handling and stuff
import json
# json will help us to convert the string to dictionary

def PrintList():
    file = open("ContactList.txt", "r")
    # opening the Contactlist file
    for line in file.readlines():
        contact = json.loads(str(line))
        # the .loads converts the string to dictionary
        print(contact["Name"])

def SerachPerson():
    pass
def deletePerson():
    pass
def AddPerson():
    pass
