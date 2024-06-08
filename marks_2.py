from tkinter import *
from tkinter import messagebox as ms
import pymysql

form=Tk()
form.geometry("1000x1000")
form.title("Student marks")

def index():
    x=t1.get()
    y=t2.get()
    a=int(t3.get())
    b=int(t4.get())
    c=int(t5.get())
    d=int(t6.get())

    tot=int(a+b+c+d)

    avg=float(int(tot)/4)

    per= (int(tot)/400)*100

    db1=pymysql.connect(host="localhost",user="root",password="",db="marks")
    cur=db1.cursor()
    cur.execute("insert into student values('%s','%s','%d','%d','%d')"%(x,y,tot,avg,per))
    db1.commit()
    ms.showinfo("welcome","data stored successfully")
    db1.close()

def data_view():
    base=Tk()
    base.geometry("500x500")
    db=pymysql.connect(host="localhost",user="root",password="",db="marks")
    cur=db.cursor()
    cur.execute("select * from student")
    m=cur.fetchall()
    x=0
    for i in m:
        for j in range(len(i)):
            l=Label(base,text=m[j])
            l.grid(row=x,column=j)    
    x=x+1
    db.commit()
    base.mainloop()

def search_data():
    sh=Tk()
    sh.geometry("500x500")
    def search_marks():
        a=en1.get()
        db=pymysql.connect(host="localhost",user="root",password="",db="marks")
        cur=db.cursor()
        cur.execute("select * from student where roll_no='%s'"%(a))
        m=cur.fetchone()
        op.insert(0,m[2])
        db.commit()
    
    def data_update():
        b=op.get()
        a=en2.get()
        db=pymysql.connect(host="localhost",user="root",password="",db="marks")
        cur=db.cursor()
        cur.execute("update student set total='%s' where roll_no ='%s'"%(b,a))
        ms.showinfo("","updated successfully")
        db.commit()
            
    en1=Entry(sh,font=("times new roman",15))
    en1.place(x=150,y=100)
    btn1=Button(sh,text="Search",font=("times new roman",15),command=search_marks)
    btn1.place(x=150,y=150)
    op=Entry(sh,font=("times new roman",15))
    op.place(x=150,y=200)
    en2=Entry(sh,font=("times new roman",15))
    en2.place(x=150,y=250)
    up=Button(sh,text="Update",font=("times new roman",15),command=data_update)
    up.place(x=150,y=300)

    sh.mainloop()



def data_delete():
    a=en3.get()
    db=pymysql.connect(host="localhost",user="root",password="",db="marks")
    cur=db.cursor()
    cur.execute("delete from student where roll_no='%s'"%(a))
    ms.showinfo("","deleted successfully")
    db.commit()
                

lb=Label(form,text="Student Details",font=("times new roman",25))
lb.pack()

lb1=Label(form,text="Name:",font=("times new roman",20))
lb1.place(x=150,y=100)
t1=Entry(form,font=("times new roman",15))
t1.place(x=250,y=105)

lb2=Label(form,text="Roll number:",font=("times new roman",20))
lb2.place(x=80,y=180)
t2=Entry(form,font=("times new roman",15))
t2.place(x=250,y=185)

lb3=Label(form,text="Marks",font=("times new roman",25))
lb3.place(x=300,y=300)

lb4=Label(form,text="BT201:",font=("times new roman",20))
lb4.place(x=150,y=380)
t3=Entry(form,font=("times new roman",15))
t3.place(x=250,y=385)

lb5=Label(form,text="BT202:",font=("times new roman",20))
lb5.place(x=150,y=460)
t4=Entry(form,font=("times new roman",15))
t4.place(x=250,y=465)

lb6=Label(form,text="BT203:",font=("times new roman",20))
lb6.place(x=150,y=540)
t5=Entry(form,font=("times new roman",15))
t5.place(x=250,y=545)

lb7=Label(form,text="BT204:",font=("times new roman",20))
lb7.place(x=150,y=620)
t6=Entry(form,font=("times new roman",15))
t6.place(x=250,y=625)

btn=Button(form,text="Submit",font=("times new roman",15),command=index)
btn.place(x=220,y=700)

view=Button(form,text="View marks",font=("times new roman",15),command=data_view)
view.place(x=220,y=750)

s=Button(form,text="Search",font=("times new roman",15),command=search_data)
s.place(x=720,y=150)

en3=Entry(form,font=("times new roman",15))
en3.place(x=720,y=300)
dele=Button(form,text="Delete",font=("times new roman",15),command=data_delete)
dele.place(x=720,y=350)
form.mainloop()