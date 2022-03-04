import sqlite3
conn=sqlite3.connect("vaccinedatabase.db")
print("DATABASE CONNECTION SUCCESSFUL")


conn.execute("Drop table if EXISTS PATIENT")
conn.execute("Drop table if EXISTS CONTACT_NO")
conn.execute("Drop table if EXISTS ROOM")
conn.execute("Drop table if EXISTS TREATMENT")
conn.execute("Drop table if EXISTS MEDICINE")

conn.execute("""Create table PATIENT
         (COWIN_ID int(10) primary key,
         NAME VARCHAR(20) not null,
         SEX varchar(10) not null,
         BLOOD_GROUP varchar(5) not null,
         DOB date not null,
         SIDE_EFFECTS varchar(100) not null,
         CONSULT_TEAM varchar(50) not null,
         CONTACT_NO varchar(20) not null   )""")
print("TABLE CREATED SUCCESSFULLY")

conn.execute("""CREATE TABLE COVID
            (COWIN_ID int(10) PRIMARY KEY,
             NODOSES int(15) not null,
             PRESCRIPTION varchar(15),
             FOREIGN KEY(COWIN_ID) REFERENCES PATIENT(COWIN_ID))
             """)
print("TABLE CREATED SUCCESSFULLY")






