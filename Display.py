# here the gui
import tkinter as tk
import json
# # calling the function in Contacts.py
# main=tk.Tk()
# # contactop.PrintList()
# # w = tk.Label(main, text='GeeksForGeeks.org!')
#
# file = open("ContactList.txt", "r")
# for line in file.readlines():
#     contact = json.loads(str(line))
#
#     # the .loads converts the string to dictionary
#     w = tk.Label(main, text=contact["Name"])
#     Lb = Listbox(top)
#     Lb.insert(1, 'Python')
#     Lb.insert(2, 'Java')
#     Lb.insert(3, 'C++')
#     Lb.insert(4, 'Any other')
#     Lb.pack()
#
#     # print(contact["Name"])
#     w.pack()
#
# main.mainloop()
def searchName(name):
    file = open("ContactList.txt", "r")
    List_of_Contacts=file.readlines()
    for line in range(len(List_of_Contacts)):
        contact = json.loads(str(List_of_Contacts[line]))
        if(contact["Name"]==name):
            return contact
def UI():
    window = tk.Tk()
    # window.attributes('-fullscreen', True)
    window.geometry('700x450')
    contact=searchName('Person2')
    window.config
    person_name=tk.Label(window,text=str(contact["Name"]))
    person_name.pack()
    name_ph_no=tk.Label(window, text=str(contact["PhoneNo"]))
    name_ph_no.pack()
    person_address=tk.Label(window, text=str(contact["Address"]))
    person_address.pack()

    # Lb1 = tk.Listbox(window)
    # Lb1.grid()
    # Lb1.insert(1, "Person2")
    # Lb1.insert(2, str(contact["PhoneNo"]))
    # Lb1.insert(3, str(contact["Address"]))
    #
    # Lb1.pack()
    window.mainloop()
def main():
    UI()

main()