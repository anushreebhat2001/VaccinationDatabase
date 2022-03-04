import tkinter
from tkinter import *
from Menupage import menu
import math
import random
import smtplib
from email.message import EmailMessage

root=None
root3=None
otpbox=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None
reg=None

users = {"username":"password"} 

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your One Time Password for your login at Vaccination Portal India. This OTP is valid for 30 minutes.\n\n\nThank you\nVaccination Portal Team"
hey = otp
msg = EmailMessage()
msg.set_content(otp)

msg['Subject'] = 'Vaccination Portal One Time Password'


#command for login button
def GET():
    
    global userbox,passbox,loginverifylabel
    S1=userbox.get()
    S2=passbox.get()
    frame = Frame()
    frame.pack(pady=3)
    loginverifylabel.pack(fill=BOTH)
    if S1 in users.keys():
        if S2 == users[S1]:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("vaccinationindiaportal@gmail.com", "vaccination@2021")
            msg['From'] = "vaccinationindiaportal@gmail.com"
            msg['To'] = S1
            server.send_message(msg)
            server.quit()
            Entry1() #if username matches password
            
        else:
            loginverifylabel["text"] = "Invalid username or password ! "
    else:
        loginverifylabel["text"] = "Invalid username or password ! "


def Entry1():
    global otpbox, verify, topframe, bottomframe, image_1,heading
    root3 = tkinter.Tk()
    root3.geometry("450x150")
    topframe = tkinter.Frame(root3)
    topframe.pack()
    bottomframe = tkinter.Frame(root3)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="WELCOME TO VACCINATION DRIVE INDIA", bg='white', fg='orange',font='Times 20 bold italic')
    otp = tkinter.Label(bottomframe, text="ENTER OTP")
    otpbox = tkinter.Entry(bottomframe, show="*")
    login1 = tkinter.Button(bottomframe, text="VERIFY OTP", command=GET1, font="arial 8 bold")
    otp.pack()
    otpbox.pack()
    login1.pack()
    root3.title("OTP VERIFICATION LOGIN")
    root3.mainloop()

def GET1():
    global otpbox,error
    S3 = str(otpbox.get())
    if(S3==OTP):
        menu()
    else:
        error=tkinter.Label(bottomframe,text="Wrong Id / Password \n TRY AGAIN",fg="red",font="bold")
        error.pack()
    
def register():
    global regbox,reguserbox,passwbox,regbox,topframe,bottomframe,registerverifylabel
    root4 = tkinter.Tk()
    root4.geometry("450x150")
    topframe = tkinter.Frame(root4)
    topframe.pack()
    bottomframe = tkinter.Frame(root4)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="WELCOME TO VACCINATION DRIVE INDIA", bg='white', fg='orange',font='Times 20 bold italic')
    reguser = tkinter.Label(topframe, text="Enter Email ID")
    regbox = tkinter.Entry(topframe)
    passw = tkinter.Label(bottomframe, text="PASSWORD")
    passwbox = tkinter.Entry(bottomframe, show="*")
    regis = tkinter.Button(bottomframe, text="CONFIRM", command=registerverify, font="arial 8 bold")
    reguser.pack()
    regbox.pack()
    passw.pack()
    passwbox.pack()
    regis.pack()
    root4.title("DATABASE REGISTER")
    registerverifylabel = Label(reg)
    registerverifylabel.pack()
    root4.mainloop()

def registerverify():
    if regbox.get() in users:
        frame=Frame()
        frame.pack(pady=2)
        registerverifylabel["text"]="This Username Is Taken"
    else:
        users[regbox.get()] = passwbox.get()
        frame=Frame()
        frame.pack(pady=2)
        registerverifylabel["text"]="Registration successful"


#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,otpbox,login,topframe,bottomframe,image_1,loginverifylabel
    root = tkinter.Tk()
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    heading = tkinter.Label(topframe, text="VACCINATION \nDRIVE INDIA",bg='white',fg='Black',font='Times 20 bold')
    heading.place(x=width, y=height, anchor="center")
    username=tkinter.Label(topframe,text="ENTER EMAIL ID",font="Times 14")
    userbox = tkinter.Entry(topframe)
    password=tkinter.Label(bottomframe,text="PASSWORD",font="Times 14")
    passbox = tkinter.Entry(bottomframe,show="*")
    login = tkinter.Button(bottomframe, text="LOGIN AND SEND OTP", command=GET,font="arial 14 bold")
    reg = tkinter.Button(bottomframe, text="REGISTER", command=register,font="arial 14 bold")
    heading.pack(pady=80)
    username.pack(pady=3)
    userbox.pack(pady=3)
    password.pack(pady=3)
    passbox.pack(pady=3)
    login.pack(pady=10)
    reg.pack(pady=10)
    root.title("DATABASE LOGIN")
    loginverifylabel = Label(root)
    loginverifylabel.pack()
    root.mainloop()

Entry()

