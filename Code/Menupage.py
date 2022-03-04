import tkinter
import sqlite3
import tkinter.messagebox
from function import P_display
from function import P_UPDATE

conn=sqlite3.connect("vaccinedatabase.db")
print("DATABASE CONNECTION SUCCESSFUL")

#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_dob=None
pat_effects=None
pat_sex=None
pat_BG=None
pat_contact=None
pat_doses=None
pat_pres=None
pat_CT=None


#EXIT for MENU
def ex():
    global root1
    root1.destroy()

#MENU BUTTONS
def menu():
    global root1,button1,button2,button3,button4,button5,m,button6
    root1=tkinter.Tk()
    width= root1.winfo_screenwidth()
    height= root1.winfo_screenheight()
    root1.geometry("%dx%d" % (width, height))
    root1.title("MAIN MENU")
    m=tkinter.Label(root1,text="MENU",font='Times 16 bold italic',fg='grey')
    button1=tkinter.Button(root1,text="1.PATIENT REGISTRATION",command=PAT,bg='light blue',fg='black')
    button2 = tkinter.Button(root1, text="2. UPDATE VACCINATION STATUS",bg='light green',fg='black',command=P_UPDATE)
    button3 = tkinter.Button(root1, text="3.DISPLAY ALL RECORDS",bg='light blue',fg='black',command=P_display)
    button4 = tkinter.Button(root1, text="4.EXIT",bg='light green',fg='black',command=ex)
    m.place(x=75,y=5)
    button1.pack(side=tkinter.TOP)
    button1.place(x=80,y=50)
    button2.pack(side=tkinter.TOP)
    button2.place(x=80,y=100)
    button3.pack(side=tkinter.TOP)
    button3.place(x=80,y=150)
    button4.pack(side=tkinter.TOP)
    button4.place(x=80, y=200)
    root1.mainloop()

p=None
#input patient form
def IN_PAT():
    global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,ce1,conn
    conn=sqlite3.connect("vaccinedatabase.db")
    conn.cursor()
    pp1=pat_ID.get()
    pp2=pat_name.get()
    pp3=pat_sex.get()
    pp4=pat_BG.get()
    pp5=pat_dob.get()
    pp6=pat_dose.get()
    pp7=pat_pres.get()
    pp8=pat_effects.get()
    pp9=pat_CT.get()
    pp10=pat_contact.get()
    conn.execute('INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?)',(pp1,pp2,pp3,pp4,pp5,pp8,pp9,pp10,))
    conn.execute('INSERT INTO COVID VALUES (?,?,?)',(pp1,pp6,pp7,))
    tkinter.messagebox.showinfo("VACCINATION DATABSE SYSTEM","DETAILS INSERTED INTO DATABASE")
    conn.commit()

#function for patient form help
def nothing():
    print("CONTACT DATABASE HEAD : Hospitalmanagement@gmail.com 8973465732 ")

def nothing1():
    print("MADE BY AARUSH,ANUSHREE AND KHUSHI")

#PATIENT FORM
back=None
SEARCH=None
DELETE=None
UPDATE=None

def PAT():
    global pat_effects, pat_BG, pat_contact, pat_pres, pat_dose, pat_dob, pat_contact, pat_ID, pat_name, pat_sex,pat_CT
    global rootp,regform,id,name,dob,sex,contact,dose,effects,ct,pres,bg,SUBMIT,menubar,filemenu,back,SEARCH,DELETE,UPDATE
    rootp=tkinter.Tk()
    rootp.title("PATIENT VACCINATION FORM")
    menubar=tkinter.Menu(rootp)
    filemenu=tkinter.Menu(menubar,tearoff=0)
    filemenu.add_command(label="NEW",command=PAT)
    helpmenu=tkinter.Menu(menubar,tearoff=0)
    helpmenu.add_command(label="HELP",command=nothing)
    helpmenu.add_command(label="ABOUT",command=nothing1)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    rootp.config(menu=menubar)
    regform=tkinter.Label(rootp,text="REGISTRATION FORM",font="Arial 16 bold")
    id=tkinter.Label(rootp,text="COWIN ID")
    pat_ID=tkinter.Entry(rootp)
    name=tkinter.Label(rootp,text="PATIENT NAME")
    pat_name = tkinter.Entry(rootp)
    sex=tkinter.Label(rootp,text="SEX")
    pat_sex=tkinter.Entry(rootp)
    dob=tkinter.Label(rootp, text="DOB (YYYY-MM-DD)")
    pat_dob=tkinter.Entry(rootp)
    bg=tkinter.Label(rootp, text="BLOOD GROUP")
    pat_BG=tkinter.Entry(rootp)
    dose=tkinter.Label(rootp, text="DOSE NUMBER (1/2)")
    pat_dose=tkinter.Entry(rootp)
    pres=tkinter.Label(rootp, text="PRESCRIPTION (IF ANY)")
    pat_pres=tkinter.Entry(rootp)
    contact=tkinter.Label(rootp, text="CONTACT NUMBER")
    pat_contact = tkinter.Entry(rootp)
    ct=tkinter.Label(rootp,text="CONSULTING TEAM / DOCTOR")
    pat_CT=tkinter.Entry(rootp)
    effects=tkinter.Label(rootp, text="SIDE EFFECTS (IF ANY)")
    pat_effects=tkinter.Entry(rootp)
    back=tkinter.Button(rootp,text="<< BACK",command=menu)
    SUBMIT=tkinter.Button(rootp,text="  SUBMIT  ",command=IN_PAT,)
    regform.pack()
    id.pack()
    pat_ID.pack()
    name.pack()
    pat_name.pack()
    sex.pack()
    pat_sex.pack()
    dob.pack()
    pat_dob.pack()
    bg.pack()
    pat_BG.pack()
    dose.pack()
    pat_dose.pack()
    pres.pack()
    pat_pres.pack()
    contact.pack()
    pat_contact.pack()
    ct.pack()
    pat_CT.pack()
    effects.pack()
    pat_effects.pack()
    SUBMIT.pack()
    back.pack(side=tkinter.LEFT)
    rootp.mainloop()

