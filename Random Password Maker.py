# This'll make a password from any characters!
# Please use this
import random
import string
import tkinter

#webList = []
passwordList = []
password = ''
def random_maker():
    global password
    length = int(entry.get())
    char = string.ascii_lowercase # lowercase letters are always included in passwords
    if display():
        char += string.ascii_uppercase # Passwords need a leader, or a capital 
    if display2():
        char += string.digits # Passwords need a number of how many
    if display3():
        char += string.punctuation # Passwords need something to end them off
    password_char = []

    for _ in range(length):
        random_letter = random.choice(char)
        password_char.append(random_letter)

    password = ''.join(password_char)
    pwd_display.config(text=password)

    return password
#print(random_maker())


# Make a window using Tkinter
window = tkinter.Tk()
window.geometry("420x420")
window.title("Random Password Generator")
window.columnconfigure(0,weight=0)
window.columnconfigure(1,weight=0)
window.columnconfigure(2,weight=0)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=0)


# Make a Frame to hold both buttons in Place
button_frame = tkinter.Frame(window)
button_frame.grid(row=6, column=3, pady=5)
"""
entry_frame = tkinter.Frame(window)
entry_frame.grid(row=5,column=3,pady=5)

label_frame= tkinter.Frame(window)
label_frame.grid
"""


# Make a Button
new_Password = tkinter.Button(button_frame,text="New Password",command= random_maker)
new_Password.config(width=12,height=1)
new_Password.config(font=("Arial",9))
new_Password.pack(side="left",padx=5)
new_Password.pack()

# Make a Copy Button 
def copy_pwd():
    #webList.append(user_input)
    passwordList.append(password) # Plan to append newly created passwords to passwordlist for user to see passwords
    #print(passwordList)
    #print(webList)
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()

copy_button = tkinter.Button(button_frame, text="Copy Password", command= copy_pwd)
copy_button.config(width=14,height=1)
copy_button.config(font=("Arial",9))
copy_button.pack(side="left",padx=5)


#Make a File Append Button
def append_Pwd():
    with open("Saved_Passwords.txt","a") as fname:
        try:
            fname.write(f"{password}\n")
            print("Password Added to File!")

        except FileNotFoundError:
            print("No File Found, creating New File...")
            fname = open("Saved_Passwords.txt","a")
            fname.write(password)
            fname.close()
            print("Password Added to File!")

file_button= tkinter.Button(button_frame, text="Add To File", command= append_Pwd)
file_button.config(width=14,height=1)
file_button.config(font=("Arial",9))
file_button.pack(side="left",padx=5)

# Making a Label
pwd_display = tkinter.Label(window,text="New Password: ")
pwd_display.config(font=("Arial",11))
pwd_display.grid(row=8,column=3,pady=3)
#pwd_display.pack()

"""
# Making a Website Label
web_display = tkinter.Label(window) 
"""


# Making an Entry
entry = tkinter.Entry(window)
entry.insert(0,"12")
entry.config(font=("Arial",11))
#entry.pack()
entry.grid(row=5,column=3)
#entry.pack(pady=2)

"""
# Website Entry
def when_enter_pressed(event):
    global user_input
    user_input = webEntry.get()

webEntry = tkinter.Entry(entry_frame)
webEntry.insert(0,"Website Name")
webEntry.config(font=("Arial",11))
webEntry.bind("<Return>",when_enter_pressed)
#webEntry.pack()
webEntry.grid(row=5,column=2)
"""



# Making 3 Check Boxes 

def display():
    if(x.get()==True):
        return True
    else:
        return False
x = tkinter.BooleanVar()

def display2():
    if(y.get()==True):
        return True
    else:
        return False
y = tkinter.BooleanVar()

def display3():
    if(z.get()==True):
        return True 
    else:
        return False
z = tkinter.BooleanVar()

checkBox = tkinter.Checkbutton(window,text="Uppercase Letters", 
                               variable=x, 
                               onvalue=True, 
                               offvalue=False,
                               command=display)
checkBox.config(font=("Arial", 12, "bold"))
checkBox.config(fg="black")
checkBox.grid(row=1,column=3)

checkBox2 = tkinter.Checkbutton(window,text="Digits", 
                               variable=y, 
                               onvalue=True, 
                               offvalue=False,
                               command=display2)
checkBox2.config(font=("Arial", 12, "bold"))
checkBox2.config(fg="black")
checkBox2.grid(row=2,column=3)

checkBox3 = tkinter.Checkbutton(window,text="Special Characters", 
                               variable=z, 
                               onvalue=True, 
                               offvalue=False,
                               command=display3)
checkBox3.config(font=("Arial", 12, "bold"))
checkBox3.config(fg="black")
checkBox3.grid(row=3,column=3)

window.mainloop()