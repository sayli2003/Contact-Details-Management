import csv
import time
from tkinter import *


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def frontpage(user_name):
    after_login_screen = Toplevel(screen)
    after_login_screen.title("Logged in!")
    after_login_screen.geometry("150x100")
    Label(after_login_screen, text="Login Success").pack()
    Button(after_login_screen, text="new C", width=10, height=1, command=lambda: add_contact(user_name)).pack()


def add_contact(user):
    global addScreen
    addScreen = Toplevel(screen)
    addScreen.title("Add New Contact")
    f = open(user, "a")
    # Fields
    Label(addScreen, text="First name: ").grid(row=0, column=0, padx=10, pady=10)
    Label(addScreen, text="Last name : ").grid(row=1, column=0, padx=10, pady=10)
    Label(addScreen, text="Phone no. : ").grid(row=2, column=0, padx=10, pady=10)
    # vars
    global firstname
    global lastname
    global phno
    firstname = StringVar()
    lastname = StringVar()
    phno = IntVar()
    phno.set('')

    # Entries
    Entry(addScreen, textvariable=firstname).grid(row=0, column=1, padx=10)
    Entry(addScreen, textvariable=lastname).grid(row=1, column=1, padx=10)
    Entry(addScreen, textvariable=phno).grid(row=2, column=1, padx=10)

    # Button
    Button(addScreen, text="Save", command=lambda: save_data(user)).grid(row=4, column=1)
    f.close()

def save_data(user):
    fn = firstname.get()
    ln = lastname.get()
    pn = phno.get()
    with open(user, 'a') as file:
        file.write(f'{fn},')
        file.write(f'{ln},')
        file.write(f'{pn}\n')
    Label(addScreen, text="saved!", fg="green").grid(row=5, column=0)
    firstname.set('')
    lastname.set('')
    phno.set('')


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
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    with open('login_info.csv', 'a') as file:
        file.write(f"\n{username_info},{password_info}")

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
            if line[0] == username1:
                flag = 1
                # print("here")
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
