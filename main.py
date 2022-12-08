import csv
import time
import json
from tkinter import *
import NewDisplay as nd

def delete3():
    screen4.destroy()
def delete5(screen):
    screen.destroy()


def delete4():
    screen5.destroy()

def frontpage(username):
    global after_login_screen
    username = username + ".txt"
    after_login_screen = Toplevel(screen)
    after_login_screen.title("Logged in!")
    after_login_screen.geometry("150x100")
    Label(after_login_screen, text="Login Success").pack()
    global ob
    ob=nd.Contact(username)
    Search_item = Entry(after_login_screen)
    Search_item.pack()
    Search_item.focus_set()
    Search_button = Button(after_login_screen, text="Search")
    Search_button.config(command=lambda: FoundItem(Search_item.get(), after_login_screen))
    Search_button.pack()
    Button(after_login_screen, text="new Contact", width=10, height=1, command=lambda: add_contact(username)).pack()
    # Button(after_login_screen, text="update Contact", width=10, height=1, command=lambda: update_contact(username)).pack()
    # Button(after_login_screen, text="delete Contact", width=10, height=1, command=lambda: delete_contact(username)).pack()
    # Button(after_login_screen, text="search Contact", width=10, height=1, command=lambda: delete_contact(username)).pack()


def FoundItem(s,screen):
    dets=ob.Details(s)
    DisplayDetails=Toplevel(screen)
    if(dets!=None):
        Label(DisplayDetails, text=dets["Name"]).pack()
        # Button(DisplayDetails, text="Call").pack()
        Label(DisplayDetails, text=dets["PhoneNo"]).pack()
        # Button(DisplayDetails, text="Email").pack()
        Label(DisplayDetails, text=dets["Address"]).pack()
        Button(DisplayDetails, text="Delete",command=lambda :Delete_contact(dets,DisplayDetails)).pack()
        Button(DisplayDetails, text="Update",command=lambda :Update_contact(dets,DisplayDetails)).pack()
    else:
        Label(DisplayDetails, text="NotFound").pack()
    Button(DisplayDetails, text="Back", width=10, height=1, command=lambda: delete5(DisplayDetails)).pack()
def add_contact(user):
    print("Entered add contact")
    global addScreen
    addScreen = Toplevel(screen)
    addScreen.title("Add New Contact")
    Label(addScreen, text="Enter contact Details").pack()
    Label(addScreen, text="Name").pack()
    Label(addScreen).pack()
    Name=Entry(addScreen)
    Name.pack()
    Name.focus_set()
    Label(addScreen).pack()
    Phone = Entry(addScreen)
    Phone.pack()
    Phone.focus_set()
    Label(addScreen).pack()
    Address = Entry(addScreen)
    Address.pack()
    Address.focus_set()
    Label(addScreen).pack()
    enter = {"Name": Name.get(), "PhoneNo": int(Phone.get()), "Address": Address.get()}
    Add=Button(addScreen, text="Add")
    Add.config( command=lambda :add(enter,user,addScreen))
    Add.pack()



def add(enter,addScreen):
    ob.append(enter)
    addScreen2 = Toplevel(screen)
    Label(addScreen2, text="Contact Added Successfully").pack()
    time.sleep(1)
    addScreen2.destroy()
    delete5(addScreen)


def Delete_contact(dets,screen):
    ob.delete(dets)
    DeleteScreen = Toplevel(screen)
    Label(DeleteScreen, text="Contact deleted Successfully").pack()
    time.sleep(1)
    DeleteScreen.destroy()
    delete5(screen)

def Update_contact(dets,screen):
    updateScreen = Toplevel(screen)
    updateScreen.title("Update Contact")
    Label(updateScreen, text="Enter contact Details").pack()
    Label(updateScreen, text="Name").pack()
    Label(updateScreen).pack()
    Name=Entry(updateScreen)
    Name.pack()
    Name.focus_set()
    Label(updateScreen).pack()
    Phone = Entry(updateScreen)
    Phone.pack()
    Phone.focus_set()
    Label(updateScreen).pack()
    Address = Entry(updateScreen)
    Address.pack()
    Address.focus_set()
    Label(updateScreen).pack()
    enter = {"Name": Name.get(), "PhoneNo": int(Phone.get()), "Address": Address.get()}
    Add=Button(updateScreen, text="update")
    Add.config( command=lambda :update(enter,dets,updateScreen))
    Add.pack()
def update(enter,dets,screen):
    ob.update(dets,enter)
    UpadateScreen = Toplevel(screen)
    Label(UpadateScreen, text="Contact deleted Successfully").pack()
    time.sleep(1)
    UpadateScreen.destroy()
    delete5(screen)

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def register_user():
    print("working")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    # file.write(username_info + "\n")
    # file.write(password_info)
    file.close()
    with open('login_info.csv', 'a') as file:
        file.write(f"{username_info},{password_info}")

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    time.sleep(0.2)
    screen1.destroy()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    with open('login_info.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        flag = 0
        for line in csv_reader:
            if(line!=[]):
                if line[0] == username1:
                    flag = 1
                    if line[1] == password1:
                        frontpage(username1)
                        time.sleep(0.1)
                        screen2.destroy()
                    else:
                        password_not_recognised()
                if flag == 0:
                    user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Contacts")
    Label(text="Contacts", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()