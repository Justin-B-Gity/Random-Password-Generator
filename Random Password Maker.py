# This'll make a password from any characters!
# Please use this
import random
import string
import tkinter

def random_maker():
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

# Make a Button
new_Password = tkinter.Button(window,text="New Password",command= random_maker)
new_Password.config(width=12,height=1)
new_Password.config(font=("Arial",9))
new_Password.grid(row=4,column=3)
#new_Password.pack()

# Making a Label
pwd_display = tkinter.Label(window,text="New Password: ")
pwd_display.config(font=("Arial",11))
pwd_display.grid(row=5,column=3)
#pwd_display.pack()

# Making an Entry
entry = tkinter.Entry()
entry.insert(0,"12")
entry.config(font=("Arial",11))
entry.grid(row=6,column=3)
#entry.pack(pady=2)

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