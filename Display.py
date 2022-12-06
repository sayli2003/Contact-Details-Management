from tkinter import *
from tkinter import ttk
import json

class Contact:
    contactList=[]
    def __init__(self,contactList):
        file = open("ContactList.txt", "r")
        for line in file.readlines():
            contact = json.loads(str(line))
            self.contactList.append(contact)

    def displayDetails(self,s,container2):
        for i in self.contactList:
            if i["Name"]==s:
                # Name = i["Name"]
                Label(container2, text=i["Name"]).pack()
                # Phno = i["PhoneNo"]
                Label(container2, text=i["PhoneNo"]).pack()
                # addr = i["Address"]
                Label(container2, text=i["Address"]).pack()
    def retNameList(self):
        names=[i["Name"] for i in self.contactList]
        return names
def searchName(name):
    file = open("ContactList.txt", "r")
    List_of_Contacts=file.readlines()
    for line in range(len(List_of_Contacts)):
        contact = json.loads(str(List_of_Contacts[line]))
        if(contact["Name"]==name):
            return contact

# def displayDetails(s,container2):
#     Label(container2,text=)
def UI(ob):
    root = Tk()
    # window.attributes('-fullscreen', True)
    root.geometry('700x450')
    contact=searchName('Person2')
    root.config(bg='white')
    container=Frame(root,pady='5',bg='white')
    container.config(bg='#3E88ED')
    search_box= Frame(container,relief=FLAT,bg='#88B4F0')
    edit = Entry(search_box,relief=FLAT,font='arial 9',bg='#88B4F0')
    edit.pack(side=LEFT, fill=Y, expand=1)
    edit.focus_set()
    butt = Button(search_box, text='Find',relief=FLAT,font='arial 9',bg='#0D6CED',fg='white',activebackground='#88B4F0',command=lambda: ob.displayDetails(edit.get(),container2))
    butt.pack(side=RIGHT)
    ttk.Separator(search_box, orient='horizontal').pack()
    search_box.pack(side=TOP,anchor='nw',fill=Y)
    for i in ob.retNameList():
        Button(container,text=i,relief=FLAT,font='arial 9',bg='#0D6CED').pack(fill=X)
    container.pack(side=LEFT,fill=Y)

    container2=Frame(root)
    container2.config(bg='pink')
    Label(container2,text='container 2',bg='pink').pack(fill=X)
    # Label(container2, text='Name :'+Name, bg='pink').pack(fill=X)
    # Label(container2, text='Phone No.: '+PHno, bg='pink').pack(fill=X)
    # Label(container2, text='Address.: ' + addr, bg='pink').pack(fill=X)
    container2.pack(fill=Y)
    root.mainloop()
def main():
    contactList=[]
    ob=Contact(contactList)
    UI(ob)

main()