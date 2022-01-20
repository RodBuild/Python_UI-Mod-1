#   KNOWN ISSUES
#   The validation of a existing user only works for users that have the same
#   email, username, password. This means users can create multiple accounts
#   using 2 repeated values and 1 different value. Hope to fix this issue when
#   I include an online database for this program
#

import tkinter as tk
import re
from tkinter import messagebox
from tkinter.constants import END, TRUE
from PIL import Image, ImageTk

WIDTH = 900             #WIDTH OF WINDOW
HEIGHT = 550            #HEIGHT OF WINDOW
USERS_FILE = "registeredUsers.txt"           #CHANGE TO THE NAME OF THE TEXT FILE YOU WANT TO USE

#Regular expression for validating an email
e_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class currentUser:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def set_user(self, username):
        self.username = username
    def get_user(self):
        return self.username
    def set_email(self, email):
        self.email = email
    def get_email(self):
        return self.email
    def set_password(self, password):
        self.password = password
    def get_password(self):
        return self.password

#Create User
logged_User = currentUser('0','0','0')

## FUNCTIONS TO BE CALLED ##
def show_frame(frame):
    frame.tkraise()

def register():
    email = ur_email.get()
    username = ur_user.get()
    password = ur_pass.get()
    bool1 = validateEmail(email)
    bool2 = searchUserInput(email,username,password)
    #RISE alert if input is blank
    if (email == "" or username == "" or password == ""):
        messagebox.showinfo("Invalid Input!", "Please fill the blank spaces.")
    #RISE alert if email is invalid
    elif(bool1 == False):
        messagebox.showinfo("Invalid Input!", "Please provide a proper email.")     
    #RISE alert if username is too short
    elif(len(username) < 5):
        messagebox.showinfo("Invalid Input!", "Username needs to be at least 5 characters long.")
    #RISE alert if password is too short
    elif(len(password) < 8):
        messagebox.showinfo("Invalid Input!", "Password needs to be at least 8 characters long.")
    #RISE alert if user already exists
    elif(bool2 == True):
        messagebox.showinfo("Invalid Input!", "User already exists.")
    #NO problems, so proceed with the user registration
    else:
        registeredUsers = open(USERS_FILE, "a")
        registeredUsers.write("\n" + email + " " + username + " " + password)
        messagebox.showinfo("Success!", "Account created succesfully!")
        show_frame(login_page)
        #Clear input
        ur_email.delete(0,END)
        ur_user.delete(0,END)
        ur_pass.delete(0,END)

def login():
    email = ul_email.get()
    username = ul_user.get()
    password = ul_pass.get()
    bool1 = searchUserInput(email,username,password)
    if (bool1 == True):
        messagebox.showinfo("Successful!", "User exists!")
        #Login Successful
        #Class Object, insert data
        logged_User.set_user(username)
        logged_User.set_email(email)
        logged_User.set_password(password)
        refreshMainPageData()
        #Move to main page
        show_frame(main_page)
        #Clear input
        ul_email.delete(0,END)
        ul_user.delete(0,END)
        ul_pass.delete(0,END)

    else:
        messagebox.showinfo("Invalid Input!", "User does not exist.")

def validateEmail(email):
    valid = False
    if(re.fullmatch(e_regex, email)):
        valid = True
    return valid

def searchUserInput(e,u,p):
    with open(USERS_FILE, "r") as f:
        for line in f:
            if(e + " " + u + " " + p) == line.strip():
                #Return TRUE is user exists
                return True
        #Return FALSE is user does not exists
        return False

def refreshMainPageData():
    #print(logged_User.get_user())
    mp_updateLabel.config(text=("Welcome back, " + logged_User.get_user() + "!"))
    mp_frame2.config(bg='orange')

def submitMainPageData():
    #print(logged_User.get_user())
    mp_updateLabel.config(text=("Data submitted!"))
    messagebox.showinfo('Great choice of fruits!', 'You selected, ' + tuple_Fruit[0] + ', ' + tuple_Fruit[1] + ', ' + tuple_Fruit[2])

def changeColor(color):
    mp_frame2.config(bg=color.get())

def languageChoice(language):
    if (language.get() == "c++"):
        messagebox.showinfo(language.get(), 'cout << Hello World! << endl')
    elif (language.get() == "python"):
        messagebox.showinfo(language.get(), 'print("Hello World")')
    else:
        messagebox.showinfo(language.get(), '<p> Hello World! </p>')
def fruitList():
    if (data4_1.get() == '1'):
        tuple_Fruit[0] = 'apple'
    else:
        tuple_Fruit[0] = ''
    
    if (data4_2.get() == '1'):
        tuple_Fruit[1] = 'banana'
    else:
        tuple_Fruit[1] = ''
    
    if (data4_3.get() == '1'):
        tuple_Fruit[2] = 'orange'
    else:
        tuple_Fruit[2] = ''
## (END) FUNCTIONS TO BE CALLED ##

## METHODS FOR TKINTER ##
window = tk.Tk()
#window.state('zoomed')
window.minsize(WIDTH, HEIGHT)
#app.maxsize(WIDTH, HEIGHT)
window.title("Login - Module #1")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#FRAMES where we can navigate through
login_page = tk.Frame(window)
register_page = tk.Frame(window)
main_page = tk.Frame(window)

#This code helps looping through the frames
for frame in (login_page, register_page, main_page):
    frame.grid(row=0,column=0,sticky='nsew')
## (END) METHODS FOR TKINTER ##


# BELOW is the design of each Page for the UI #

#==================Login Page code
#BACKGROUND picture
img = ImageTk.PhotoImage(Image.open("background_login_Page.jpg"))
lg_back=tk.Label(login_page, image=img)
lg_back.place(relheight=1,relwidth=1)

#CREATE labels for entry boxes
tk.Label(login_page, text="Email", font=('Bahnschrift SemiBold', 25)).place(relx=0.18, rely=0.1, relheight=0.1, relwidth=0.2)
tk.Label(login_page, text="Username", font=('Bahnschrift SemiBold', 25)).place(relx=0.18, rely=0.3, relheight=0.1, relwidth=0.2)
tk.Label(login_page, text="Password", font=('Bahnschrift SemiBold', 25)).place(relx=0.18, rely=0.5, relheight=0.1, relwidth=0.2)

#CREATE entry boxes (email, username, password)
ul_email = tk.Entry(login_page, bd=5, font=('Bahnschrift SemiBold', 25))
ul_email.place(relx=0.38, rely=0.1, relheight=0.1, relwidth=0.4)
ul_user = tk.Entry(login_page, bd=5, font=('Bahnschrift SemiBold', 25))
ul_user.place(relx=0.38, rely=0.3, relheight=0.1, relwidth=0.4)
ul_pass = tk.Entry(login_page, bd=5, font=('Bahnschrift SemiBold', 25), show='*')
ul_pass.place(relx=0.38, rely=0.5, relheight=0.1, relwidth=0.4)

#CREATE button to manupulate data
tk.Button(login_page, text="Log in", font=('Bahnschrift SemiBold', 25), command=lambda:login(), bd=6).place(relx=0.42, rely=0.7, relheight=0.11, relwidth=0.12)
tk.Button(login_page, text="Sign up", font=('Bahnschrift SemiBold', 25), command=lambda:show_frame(register_page), bd=6).place(relx=0.38, rely=0.85, relheight=0.11, relwidth=0.2)


#==================Register Page code
#CREATE labels for extry boxes
tk.Label(register_page, text="Email", font=('Bahnschrift SemiBold', 25)).place(relx=0.18, rely=0.1, relheight=0.1, relwidth=0.2)
tk.Label(register_page, text="Username", font=('Bahnschrift SemiBold', 25)).place(relx=0.18, rely=0.3, relheight=0.1, relwidth=0.2)
tk.Label(register_page, text="Password", font=('Bahnschrift SemiBold', 25)).place(relx=0.18, rely=0.5, relheight=0.1, relwidth=0.2)

#GO BACK button
ur_goBack_img = ImageTk.PhotoImage(Image.open("login-rounded--v1.jpg"))
ur_goBack_btn = tk.Button(register_page, image=ur_goBack_img, command=lambda:show_frame(login_page), borderwidth=0)
ur_goBack_btn.place(relx=0.02,rely=0.02)

#CREATE entry boxes (email, username, password)
ur_email = tk.Entry(register_page, bd=5, font=('Bahnschrift SemiBold', 25))
ur_email.place(relx=0.38, rely=0.1, relheight=0.1, relwidth=0.4)
ur_user = tk.Entry(register_page, bd=5, font=('Bahnschrift SemiBold', 25))
ur_user.place(relx=0.38, rely=0.3, relheight=0.1, relwidth=0.4)
ur_pass = tk.Entry(register_page, bd=5, font=('Bahnschrift SemiBold', 25))
ur_pass.place(relx=0.38, rely=0.5, relheight=0.1, relwidth=0.4)

#CREATE button to manupulate data
tk.Button(register_page, text="Register", font=('Bahnschrift SemiBold', 25), command=lambda:register(), bd=6).place(relx=0.42, rely=0.7, relheight=0.11, relwidth=0.18)


#==================Main Page code
#CREATE currentUser Object to store further data.
mp_frame1 = tk.Frame(main_page, highlightbackground="black", highlightthickness=2)
mp_frame1.place(relx=0.01,rely=0.01, relheight=0.2, relwidth=0.75)
mp_frame2 = tk.Frame(main_page, bg='orange')
mp_frame2.place(relx=0.01,rely=0.25,relheight=0.7,relwidth=0.75)

#GO BACK button
mp_goBack_img = ImageTk.PhotoImage(Image.open("logout-rounded-left--v1.jpg"))
mp_goBack_btn = tk.Button(main_page, image=mp_goBack_img, command=lambda:show_frame(login_page), borderwidth=0)
mp_goBack_btn.place(relx=0.02,rely=0.02)

#Main label
mp_updateLabel = tk.Label(mp_frame1,text='no_updated',font=('Bahnschrift SemiBold', 25))
mp_updateLabel.place(relx=0.15,rely=0.27)
mp_bt1 = tk.Button(mp_frame1, text="Refresh Data",command=lambda:refreshMainPageData())
mp_bt1.place(relx=0.8,rely=0.2)
mp_bt2 = tk.Button(mp_frame1, text="Submit Data",command=lambda:submitMainPageData())
mp_bt2.place(relx=0.8,rely=0.6)

## Radio Buttons ##
#data1 is the selection of favorite pet species
data1 = tk.StringVar()
mp_data1_label = tk.Label(mp_frame2,text='Favorite Pet:', font=('Bahnschrift SemiBold', 20), bg='orange')
mp_data1_label.place(relx=0.1, rely=0.1)
mp_data1_btn1 = tk.Radiobutton(mp_frame2, text='Cat', variable=data1, value='cat',  bg='orange', font=('Bahnschrift SemiBold', 20))
mp_data1_btn1.place(relx=0.4,rely=0.1)
mp_data1_btn2 = tk.Radiobutton(mp_frame2, text='Dog', variable=data1, value='dog',  bg='orange', font=('Bahnschrift SemiBold', 20))
mp_data1_btn2.place(relx=0.6,rely=0.1)
mp_data1_btn3 = tk.Radiobutton(mp_frame2, text='Fish', variable=data1, value='fish',  bg='orange', font=('Bahnschrift SemiBold', 20))
mp_data1_btn3.place(relx=0.8,rely=0.1)

#data2 is the selection of favorite color
data2 = tk.StringVar()
mp_data2_label = tk.Label(mp_frame2,text='Color:', font=('Bahnschrift SemiBold', 20), bg='orange')
mp_data2_label.place(relx=0.1, rely=0.3)
mp_data2_btn1 = tk.Radiobutton(mp_frame2, text='Red', variable=data2, value='red', bg='orange', command=lambda:changeColor(data2), font=('Bahnschrift SemiBold', 20))
mp_data2_btn1.place(relx=0.4,rely=0.3)
mp_data2_btn2 = tk.Radiobutton(mp_frame2, text='Yellow', variable=data2, value='yellow', bg='orange', command=lambda:changeColor(data2), font=('Bahnschrift SemiBold', 20))
mp_data2_btn2.place(relx=0.6,rely=0.3)
mp_data2_btn3 = tk.Radiobutton(mp_frame2, text='Blue', variable=data2, value='blue',  bg='orange', command=lambda:changeColor(data2), font=('Bahnschrift SemiBold', 20))
mp_data2_btn3.place(relx=0.8,rely=0.3)

#data3 is the selection of favorite programming language
data3 = tk.StringVar()
mp_data3_label = tk.Label(mp_frame2,text='Programming:', font=('Bahnschrift SemiBold', 20), bg='orange')
mp_data3_label.place(relx=0.1, rely=0.5)
mp_data3_btn1 = tk.Radiobutton(mp_frame2, text='C++', variable=data3, value='c++',  bg='orange', command=lambda:languageChoice(data3), font=('Bahnschrift SemiBold', 20))
mp_data3_btn1.place(relx=0.4,rely=0.5)
mp_data3_btn2 = tk.Radiobutton(mp_frame2, text='Python', variable=data3, value='python',  bg='orange', command=lambda:languageChoice(data3), font=('Bahnschrift SemiBold', 20))
mp_data3_btn2.place(relx=0.6,rely=0.5)
mp_data3_btn3 = tk.Radiobutton(mp_frame2, text='HTML', variable=data3, value='html',  bg='orange', command=lambda:languageChoice(data3), font=('Bahnschrift SemiBold', 20))
mp_data3_btn3.place(relx=0.8,rely=0.5)

#data4 is the selection of favorite fruits (multiple can be selected)
tuple_Fruit = ['','','']
data4_1 = tk.StringVar()
data4_2 = tk.StringVar()
data4_3 = tk.StringVar()
mp_data4_label = tk.Label(mp_frame2,text='Fruits:', bg='orange', font=('Bahnschrift SemiBold', 20), )
mp_data4_label.place(relx=0.1, rely=0.7)
mp_data4_btn1 = tk.Checkbutton(mp_frame2, text='Apple', variable=data4_1, bg='orange', command=lambda:fruitList(),font=('Bahnschrift SemiBold', 20))
mp_data4_btn1.place(relx=0.4,rely=0.7)
mp_data4_btn2 = tk.Checkbutton(mp_frame2, text='Banana', variable=data4_2, bg='orange', command=lambda:fruitList(),font=('Bahnschrift SemiBold', 20))
mp_data4_btn2.place(relx=0.6,rely=0.7)
mp_data4_btn3 = tk.Checkbutton(mp_frame2, text='Orange', variable=data4_3, bg='orange', command=lambda:fruitList(),font=('Bahnschrift SemiBold', 20))
mp_data4_btn3.place(relx=0.8,rely=0.7)


show_frame(login_page)




window.mainloop()