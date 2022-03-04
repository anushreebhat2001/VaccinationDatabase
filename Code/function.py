import tkinter
import sqlite3
import tkinter.messagebox
conn=sqlite3.connect("vaccinedatabase.db")
#variables
rootU=None
rootD=None
rootS=None
head=None
inp_s=None
searchB=None
#display/search button

def Search_button():
    global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
    c1=conn.cursor()
    inp_s=entry.get()
    rootS = tkinter.Tk()
    width= rootS.winfo_screenwidth()
    height= rootS.winfo_screenheight()
    p=list(c1.execute('select * from PATIENT where COWIN_ID=?',(inp_s,)))
    if (len(p)==0):
        errorS=tkinter.Label(rootS,text="PATIENT RECORD NOT FOUND")
        errorS.pack()
    else:
        t=c1.execute('SELECT * FROM PATIENT NATURAL JOIN COVID where COWIN_ID=?',(inp_s,));
        for i in t:
            l1=tkinter.Label(rootS,text="COWIN ID ",fg='green')
            dis1=tkinter.Label(rootS,text=i[0])
            l2=tkinter.Label(rootS,text="PATIENT NAME",fg='green')
            dis2=tkinter.Label(rootS,text=i[1])
            l3=tkinter.Label(rootS,text="PATIENT SEX",fg='green')
            dis3=tkinter.Label(rootS,text=i[2])
            l4=tkinter.Label(rootS,text="PATIENT BLOOD GROUP",fg='green')
            dis4=tkinter.Label(rootS,text=i[3])
            l5=tkinter.Label(rootS,text="PATIENT DATE OF BIRTH",fg='green')
            dis5=tkinter.Label(rootS,text=i[4])
            l6=tkinter.Label(rootS,text="SIDE EFFECTS (IF ANY)",fg='green')
            dis6=tkinter.Label(rootS,text=i[5])
            l7=tkinter.Label(rootS,text="PATIENT DOCTOR/TEAM",fg='green')
            dis7=tkinter.Label(rootS,text=i[6])
            l8=tkinter.Label(rootS,text="CONTACT NUMBER",fg='green')
            dis8=tkinter.Label(rootS,text=i[7])
            l9=tkinter.Label(rootS,text="DOSE NUMBER (1/2)",fg='green')
            dis9=tkinter.Label(rootS,text=i[8])
            l10=tkinter.Label(rootS,text="PRESCRIPTION (IF ANY)",fg='green')
            dis10=tkinter.Label(rootS,text=i[9])
            l1.pack()
            dis1.pack()
            l2.pack()
            dis2.pack()
            l3.pack()
            dis3.pack()
            l4.pack()
            dis4.pack()
            l5.pack()
            dis5.pack()
            l6.pack()
            dis6.pack()
            l7.pack()
            dis7.pack()
            l8.pack()
            dis8.pack()
            l9.pack()
            dis9.pack()
            l10.pack()
            dis10.pack()
            conn.commit()


def eXO():
    rootS.destroy()

##search window
def P_display():
    global rootS,head,inp_s,entry,searchB
    rootS=tkinter.Tk()
    rootS.title("DISPLAY")
    head=tkinter.Label(rootS,text="ENTER PATIENT ID TO DISPLAY",fg="red")
    entry=tkinter.Entry(rootS)
    searchB=tkinter.Button(rootS,text='SEARCH',command=Search_button)
    menubar= tkinter.Menu(rootS)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=P_display)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=eXO)
    menubar.add_cascade(label="File", menu=filemenu)
    rootS.config(menu=menubar)
    head.pack()
    entry.pack()
    searchB.pack()
    rootS.mainloop()

inp_d=None
entry1=None
errorD=None
disd1=None




##variables for update

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

def up1():
    global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, ue1, conn
    conn.cursor()
    u1 = pat_ID.get()
    u2 = pat_name.get()
    u3 = pat_sex.get()
    u4 = pat_dob.get()
    u5 = pat_BG.get()
    u6 = pat_doses.get()
    u7 = pat_pres.get()
    u8 = pat_contact.get()
    u9 = pat_CT.get()
    u10 = pat_effects.get()
    conn = sqlite3.connect("vaccinedatabase.db")
    p = list(conn.execute("Select * from PATIENT where COWIN_ID=?", (u1,)))
    if len(p) != 0:
        conn.execute('UPDATE PATIENT SET NAME=?,SEX=?,DOB=?,BLOOD_GROUP=?,SIDE_EFFECTS=?,CONSULT_TEAM=?,CONTACT_NO=? where COWIN_ID=?', ( u2, u3, u4, u5, u10, u9, u8,u1,))
        conn.execute('UPDATE COVID  set NODOSES =?,PRESCRIPTION=? WHERE COWIN_ID=?', ( u6, u7,u1,))
        tkinter.messagebox.showinfo("VACCINATION DATABSE SYSTEM", "DETAILS UPDATED INTO DATABASE")
        conn.commit()

    else:
        tkinter.messagebox.showinfo("VACCINATION DATABSE SYSTEM", "PATIENT IS NOT REGISTERED")

labelu=None
bu1=None

def EXITT():
    rootU.destroy()

##-----PATIENT UPDATE SCREEN -----##
def P_UPDATE():
    global pat_effects, pat_BG, pat_doses, pat_pres, pat_CT, pat_dob, pat_contact, pat_ID, pat_name, pat_sex
    global rootU, regform, id, name, dob, sex, contact, ct, effects, pres, doses, bg, SUBMIT, menubar, filemenu, p1f, p2f,HEAD
    rootU = tkinter.Tk()
    rootU.title("UPDATE WINDOW")
    menubar = tkinter.Menu(rootU)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=P_UPDATE)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=EXITT)
    rootU.config(menu=menubar)
    menubar.add_cascade(label="File", menu=filemenu)
    HEAD=tkinter.Label(rootU,text="ENTER NEW DETAILS TO UPDATE",bg='black',fg='white')
    id = tkinter.Label(rootU, text="COWIN ID")
    pat_ID = tkinter.Entry(rootU)
    name = tkinter.Label(rootU, text="PATIENT NAME")
    pat_name = tkinter.Entry(rootU)
    sex = tkinter.Label(rootU, text="SEX")
    pat_sex = tkinter.Entry(rootU)
    dob = tkinter.Label(rootU, text="DOB (YYYY-MM-DD)")
    pat_dob = tkinter.Entry(rootU)
    bg = tkinter.Label(rootU, text="BLOOD GROUP")
    pat_BG = tkinter.Entry(rootU)
    doses = tkinter.Label(rootU, text="DOSE NUMBER")
    pat_doses = tkinter.Entry(rootU)
    pres =  tkinter.Label(rootU, text="PRESCRIPTION (IF ANY)")
    pat_pres = tkinter.Entry(rootU)
    contact = tkinter.Label(rootU, text="CONTACT NUMBER")
    pat_contact = tkinter.Entry(rootU)
    ct = tkinter.Label(rootU, text="CONSULTING TEAM / DOCTOR")
    pat_CT = tkinter.Entry(rootU)
    effects = tkinter.Label(rootU, text="SIDE EFFECTS (IF ANY)")
    pat_effects = tkinter.Entry(rootU)
    SUBMIT=tkinter.Button(rootU,text="SUBMIT",command=up1)
    HEAD.pack()
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
    doses.pack()
    pat_doses.pack()
    contact.pack()
    pat_contact.pack()
    pres.pack()
    pat_pres.pack()
    ct.pack()
    pat_CT.pack()
    effects.pack()
    pat_effects.pack()
    SUBMIT.pack()
    rootU.mainloop()
