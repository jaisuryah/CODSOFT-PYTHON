from tkinter import *
from random import randint

#list of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*']

#function to generate a password using above list
def generate():
    password = ""

    password_field.delete(0, END)

    password_field.config(show='*')

    show_password_btn.config(text="Show Password")

    for i in range(0, length.get()):
        index = randint(0, len(letters) - 1)
        password += letters[index]

    password_field.insert(0, password)

#this will be triggered when user hits enter
def generateenter(event):
    generate()

#this function will show the password instead of showing it in stream of ****
def showpassword():
    if password_field.cget('show') == '*':
        password_field.config(show="")
        show_password_btn.config(text="Hide Password")
    else:
        password_field.config(show="*")
        show_password_btn.config(text="Show Password")

#initialize gui
root = Tk()

#set minimum and initial size of gui window
root.geometry("350x200")
root.minsize(width=100, height=100)

#set title and icon
root.title("Password Generator")
root.wm_iconbitmap("password.ico")

#heading
heading = Label(root, text="Password Generator", font="Helvetica 15 bold italic")
heading.pack(pady=10)

#a frame just like a div in html to include prompt and input field
f1 = Frame(root)
f1.pack(pady=10)

prompt = Label(f1, text="Enter password length")
prompt.pack(side=LEFT, padx=10)

#variable to store length
length = IntVar()

field = Entry(f1, textvariable=length)
field.pack(side=LEFT)
field.bind('<Return>', generateenter)

#button to generate password
generate_btn = Button(root, fg="black", text="Generate", command=generate)
generate_btn.pack(pady=10)

#second frame to hold password field and show password button
f2 = Frame(root)
f2.pack(pady=10)

#password field
password_field = Entry(f2, show='*')
password_field.pack(side=LEFT, padx=10)

#button to hide and show password
show_password_btn = Button(f2, fg='black', text="Show Password", command=showpassword)
show_password_btn.pack(side=LEFT, padx=10)

#start gui
root.mainloop()
