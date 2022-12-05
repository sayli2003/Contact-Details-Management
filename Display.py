# here the gui
# import Contacts as contactop
import tkinter as tk
import json
# calling the function in Contacts.py
main=tk.Tk()
# contactop.PrintList()
# w = tk.Label(main, text='GeeksForGeeks.org!')

file = open("ContactList.txt", "r")
for line in file.readlines():
    contact = json.loads(str(line))

    # the .loads converts the string to dictionary
    w = tk.Label(main, text=contact["Name"])
    # print(contact["Name"])
    w.pack()

main.mainloop()
