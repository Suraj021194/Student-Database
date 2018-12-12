from tkinter import *
from pymysql import *
from tkinter import messagebox as msg
from tkinter import ttk

def main():
    root = Tk()
    w = Window1(root)
    root.mainloop()

class Window1:
    def __init__(self,master):
        self.master = master

        self.master.geometry("800x600+132+168")
        self.master.configure(bg="blue")

        self.frame = Frame(self.master,height=600,width=800,bg="cyan")
        self.frame.pack()

        self.label = Label(self.frame,text = "Student Database Login Page",bg="cyan",width=40,font=("Times New Roman",40,"bold"),anchor=W)
        self.label.place(x=60,y=0)

        self.label1 = Label(self.frame, text="Username", bg="cyan", width=30,
                           font=("Times New Roman", 30, "bold"), anchor=W)
        self.label1.place(x=120, y=200)

        self.label2 = Label(self.frame, text="Password", bg="cyan", width=30,
                           font=("Times New Roman", 30, "bold"), anchor=W)
        self.label2.place(x=120, y=300)

        self.user_text = StringVar()
        self.user_entry = Entry(self.frame,width=20,textvariable = self.user_text,font=("Times New Roman", 25, "bold"))
        self.user_entry.place(x=350,y=200)

        self.pass_text = StringVar()
        self.pass_entry1 = Entry(self.frame, width=20,textvariable=self.pass_text,font=("Times New Roman", 25, "bold"))
        self.pass_entry1.place(x=350, y=300)

        self.but1login = Button(self.frame,text= "Login",command=self.Login_System,anchor=CENTER,font=("Times New Roman", 25, "bold"))
        self.but1login.place(x=200,y=400)
        self.but1login.bind("<Return>",self.Login_System)

        self.but2login = Button(self.frame, text="EXIT", command=self.close, anchor=CENTER,
                                font=("Times New Roman", 25, "bold"))
        self.but2login.place(x=450, y=400)

        self.user_entry.focus()



    def Login_System(self,k_enter):
        self.u = str(self.user_text.get())
        self.p = str(self.pass_text.get())
        try:
            con = connect(host="localhost",user="root",password="Suraj1234",db="college")
            cursor = con.cursor()
            query = "select  * from admin"
            cursor.execute(query)
            self.res = cursor.fetchall()
            for self.row in self.res:
                if self.u ==self.row[1] and self.p ==self.row[2]:
                    self.master.destroy()
                    self.newwindow = Tk()
                    self.app = Window2(self.newwindow)
                else:
                    msg.askyesno("Invalid Login,Please enter correct password")
                    self.user_text.set("")
                    self.pass_text.set("")
                    self.user_entry.focus()

        except DatabaseError as e:
            if con:
                con.rollback()
                msg.showinfo("Invalid username and password")

        finally:
            if cursor:
                cursor.close()

            if con:
                con.close()


    def close(self):
            quit()

class Window2:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x600+132+168')
        self.master.resizable(width=False, height=False)



        self.frame = Frame(master, width=800, height=600, bg="steelblue")
        self.frame.pack()

        self.heading = Label(self.frame,text = "Student Database System",bg="steelblue",width=40,height=1,font=("Times New Roman",50,"bold"),anchor=W)
        self.heading.place(x=30, y=20)

        self.insertbutton = Button(self.frame, text="Insert Student",command=self.insert, font=("arial", 20, "bold"), fg="black", bg="lightgreen",
                               anchor=CENTER)
        self.insertbutton.place(x=20, y=300)

        self.searchbutton = Button(self.frame, text="Update Student",command=self.Update_value,font=("arial", 20, "bold"), fg="black", bg="lightgreen")
        self.searchbutton.place(x=300, y=300)

        self.viewbutton = Button(self.frame, text="Update Student", command=self.Update_value,
                                   font=("arial", 20, "bold"), fg="black", bg="lightgreen")
        self.searchbutton.place(x=600, y=500)

        self.closebutton = Button(self.frame, text="Close",command=self.close,font=("arial", 20, "bold"), fg="black", bg="lightgreen")
        self.closebutton.place(x=800, y=300)

    def insert(self):
        self.master.destroy()
        self.w2 = Tk()
        self.a = Window3(self.w2)

    def Update_value(self):
        self.master.destroy()
        self.w3 = Tk()
        self.a = Window4(self.w3)

    def View_all(self):
        self.master.destroy()
        self.w4 = Tk()
        self.a = Window5(self.w4)

    def close(self):
            quit()


class Window3:
    def __init__(self,master):
        self.master = master
        self.master.geometry('800x600+132+168')
        self.master.resizable(height=False,width=False)

        self.frame = Frame(self.master,height=600,width=800,bg="cyan")
        self.frame.pack()

        self.label = Label(self.frame, text="Insert Student", font=("arial", 40, "bold"),width=20, fg="black", bg="cyan", anchor=W)
        self.label.place(x=150, y=0)


        self.label1 = Label(self.frame, text="Roll", font=("arial", 20, "bold"), fg="black", bg="cyan", anchor=W)
        self.label1.place(x=100, y=100)

        self.label2 = Label(self.frame, text="Name", font=("arial", 20, "bold"), fg="black", bg="cyan")
        self.label2.place(x=100, y=150)

        self.label3 = Label(self.frame, text="Course", font=("arial", 20, "bold"), fg="black", bg="lightgreen")
        self.label3.place(x=100, y=200)

        self.label4 = Label(self.frame, text="Fee", font=("arial", 20, "bold"), bg="lightgreen", fg="black")
        self.label4.place(x=100, y=250)

        self.label5 = Label(self.frame, text="Age", font=("arial", 20, "bold"), bg="lightgreen", fg="black")
        self.label5.place(x=100, y=300)

        self.label6 = Label(self.frame, text="Department", font=("arial", 20, "bold"), bg="lightgreen", fg="black")
        self.label6.place(x=100, y=350)

        self.label7 = Label(self.frame, text="Year", font=("arial", 20, "bold"), bg="lightgreen", fg="black")
        self.label7.place(x=100, y=400)

        self.roll_entry = IntVar()
        self.entry1 = Entry(self.frame, textvariable=self.roll_entry, width=15, font=("arial", 20, "bold"))
        self.entry1.place(x=300, y=100)

        self.name_entry = StringVar()
        self.entry2 = Entry(self.frame, textvariable=self.name_entry, width=15, font=("arial", 20, "bold"))
        self.entry2.place(x=300, y=150)

        self.course_entry = StringVar()
        self.entry3 = Entry(self.frame, textvariable=self.course_entry, width=15, font=("arial", 20, "bold"))
        self.entry3.place(x=300, y=200)

        self.fee_entry = IntVar()
        self.entry4 = Entry(self.frame, textvariable=self.fee_entry, width=15, font=("arial", 20, "bold"))
        self.entry4.place(x=300, y=250)

        self.age_entry = IntVar()
        self.entry5 = Entry(self.frame, textvariable=self.age_entry, width=15, font=("arial", 20, "bold"))
        self.entry5.place(x=300, y=300)

        self.department_entry = StringVar()
        self.entry6 = Entry(self.frame, textvariable=self.department_entry, width=15, font=("arial", 20, "bold"))
        self.entry6.place(x=300, y=350)

        self.year_entry = IntVar()
        self.entry7 = Entry(self.frame, textvariable=self.year_entry, width=15, font=("arial", 20, "bold"))
        self.entry7.place(x=300, y=400)

        self.addbutton = Button(self.frame, text="Add", command=self.add, font=("arial", 25, "bold"), fg="black")
        self.addbutton.place(x=150, y=500)

        self.closebutton = Button(self.frame, text="Close", command=self.close, font=("arial", 25, "bold"), fg="black")
        self.closebutton.place(x=400, y=500)

    def add(self):
        self.val1 = self.roll_entry.get()
        self.val2 = self.name_entry.get()
        self.val3 = self.course_entry.get()
        self.val4 = self.fee_entry.get()
        self.val5 = self.age_entry.get()
        self.val6 = self.department_entry.get()
        self.val7 = self.year_entry.get()

        if self.val1 == " " or self.val2 == " " or self.val3 == " " or self.val4 == " " or self.val5 == " ":
            msg.showinfo("Warning", "Please Fill the up all Boxes")
        else:
            try:
                con = connect(host="localhost", user="root", password="Suraj1234", db="college")
                cursor = con.cursor()
                query = "insert into student(Roll,Name,Course,Fees,Age," \
                        "Department,Year)values(%d,'%s','%s',%d,%d,'%s',%d)"
                cursor.execute(query %(self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7))
                con.commit()
                msg.showinfo("One row inserted")

            except DatabaseError as e:
                if con:
                    con.rollback()
                    msg.showinfo("Something gone wrong ")

            finally:
                if cursor:
                    cursor.close()

                if con:
                    con.close()


    def close(self):
            quit()


class Window4:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1000x800+268+32')
        self.master.resizable(height=False, width=False)

        self.frame = Frame(self.master, height=800, width=1000, bg="cyan")
        self.frame.pack()

        self.label = Label(self.frame, text="Update Student", font=("arial", 20, "bold"), fg="black", bg="cyan", anchor=W)
        self.label.place(x=200, y=10)

        self.label1 = Label(self.frame, text="Enter Roll Number", font=("arial", 20, "bold"), fg="black", bg="cyan", anchor=W)
        self.label1.place(x=20, y=100)

        self.roll_entry = IntVar()
        self.entry = Entry(self.frame, textvariable=self.roll_entry, width=20, font=("arial", 20, "bold"))
        self.entry.place(x=400, y=100)

        self.serachbutton = Button(self.frame, text="Search", command=self.search, font=("arial", 20, "bold"), fg="black")
        self.serachbutton.place(x=200, y=200)



    def search(self):
        self.val1 = self.roll_entry.get()

        try:
            con = connect(host="localhost", user="root", password="Suraj1234", db="college")
            cursor = con.cursor()
            query = "select * from student where Roll = %d"
            cursor.execute(query %(self.val1,))
            self.res = cursor.fetchall()
            for self.row in self.res:
                self.uroll_entry1 =  self.row[0]
                self.uname_entry2 = self.row[1]
                self.ucourse_entry3 = self.row[2]
                self.ufee_entry4 = self.row[3]
                self.uage_entry5 = self.row[4]
                self.udepartment_entry6 = self.row[5]
                self.uyear_entry7 = self.row[6]


            self.label1 = Label(self.frame, text="Roll", font=("arial", 20, "bold"), fg="black", bg="cyan",
                                    anchor=W)
            self.label1.place(x=10, y=300)

            self.label2 = Label(self.frame, text="Name", font=("arial", 20, "bold"), fg="black", bg="cyan")
            self.label2.place(x=10, y=350)

            self.label3 = Label(self.frame, text="Course", font=("arial", 20, "bold"), fg="black", bg="lightgreen")
            self.label3.place(x=10, y=400)

            self.label4 = Label(self.frame, text="Fee", font=("arial", 20, "bold"), bg="lightgreen", fg="black")
            self.label4.place(x=10, y=450)

            self.label5 = Label(self.frame, text="Age", font=("arial", 20, "bold"), bg="lightgreen",
                                    fg="black")
            self.label5.place(x=10, y=500)

            self.label6 = Label(self.frame, text="Department", font=("arial", 20, "bold"), bg="lightgreen",
                                    fg="black")
            self.label6.place(x=10, y=550)

            self.label7 = Label(self.frame, text="Year", font=("arial", 20, "bold"), bg="lightgreen",
                                    fg="black")
            self.label7.place(x=10, y=600)

            self.entry1 = Entry(self.frame, width=20, font=("arial", 20, "bold"))
            self.entry1.place(x=300, y=300)
            self.entry1.insert(END,str(self.uroll_entry1))

            self.entry2 = Entry(self.frame ,width=20, font=("arial", 20, "bold"))
            self.entry2.place(x=300, y=350)
            self.entry2.insert(END, str(self.uname_entry2))

            self.entry3 = Entry(self.frame,  width=20, font=("arial", 20, "bold"))
            self.entry3.place(x=300, y=400)
            self.entry3.insert(END, str(self.ucourse_entry3))

            self.entry4 = Entry(self.frame, width=20, font=("arial", 20, "bold"))
            self.entry4.place(x=300, y=450)
            self.entry4.insert(END, str(self.ufee_entry4))


            self.entry5 = Entry(self.frame, width=20, font=("arial", 20, "bold"))
            self.entry5.place(x=300, y=500)
            self.entry5.insert(END, str(self.uage_entry5))


            self.entry6 = Entry(self.frame,  width=20, font=("arial", 20, "bold"))
            self.entry6.place(x=300, y=550)
            self.entry6.insert(END, str(self.udepartment_entry6))

            self.entry7 = Entry(self.frame,  width=20, font=("arial", 20, "bold"))
            self.entry7.place(x=300, y=600)
            self.entry7.insert(END, str(self.uyear_entry7))

            self.updatebutton = Button(self.frame, text="Update", command=self.update, font=("arial", 20, "bold"),
                                          fg="black")
            self.updatebutton.place(x=200, y=700)

            self.deletebutton = Button(self.frame, text="Delete", command=self.delete, font=("arial", 20, "bold"),
                                          fg="black")
            self.deletebutton.place(x=100, y=700)

            con.commit()
            msg.showinfo("","Value are search")

        except DatabaseError as e:
            if con:
                con.rollback()
                msg.showinfo("Something gone wrong ")


        finally:
            if cursor:
                cursor.close()

            if con:
                con.close()

    def update(self):
        self.var1 = int(self.entry1.get())
        self.var2 = (self.entry2.get())
        self.var3 = (self.entry3.get())
        self.var4 = int(self.entry4.get())
        self.var5 = int(self.entry5.get())
        self.var6 = (self.entry6.get())
        self.var7 = int(self.entry7.get())
        print(type(self.var1),type(self.val1),type(self.var3),type(self.var4),type(self.var5),type(self.var6),type(self.var7),self.var1,type(self.var2),self.val1,self.var2,self.var3,self.var4,self.var5,self.var6,self.var7,self.val1)
        try:
            con = connect(host="localhost", user="root", password="Suraj1234", db="college")
            cursor = con.cursor()
            query = "update student set roll=%d or name='%s'or course ='%s' or fees=%d or age=%d or " \
                    "  department='%s' or year=%d where roll=%d"
            print(self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.var7, self.val1)
            cursor.execute(query %(self.var1,self.var2,self.var3,self.var4,self.var5,self.var6,self.var7,int(self.val1),))
            con.commit()
            msg.showinfo("","Data are updated")
        except DatabaseError as e:
            if con:
                con.rollback()
                msg.showinfo("Value are not updated",e)

        finally:
            if cursor:
                cursor.close()

            if con:
                con.close()

    def delete(self):
        try:
            con = connect(host="localhost", user="root", password="Suraj1234", db="college")
            cursor = con.cursor()
            query = "delete  from student where roll = %d"
            cursor.execute(query %(self.val1, ))
            con.commit()
            msg.showinfo(" ","one row  Deleted")
            self.entry1.destroy()
            self.entry2.destroy()
            self.entry3.destroy()
            self.entry4.destroy()
            self.entry5.destroy()
            self.entry6.destroy()
            self.entry7.destroy()

        except DatabaseError as e:
            if con:
                con.rollback()
                msg.showinfo("","Value are not updated")

        finally:
            if cursor:
                cursor.close()

            if con:
                con.close()
class Window5:
    def __init__(self,master):
        self.master = master
        self.master.geometry('800x600+132+168')
        self.master.resizable(height=False,width=False)
        try:
            con = connect(host="localhost", user="root", password="Suraj1234", db="college")
            cursor = con.cursor()
            query = "delete  from student where roll = %d"
            cursor.execute(query %(self.val1, ))
            con.commit()
            msg.showinfo(" ","one row  Deleted")
        except DatabaseError as e:
            if con:
                con.rollback()
                msg.showinfo("","Value are searched")

        finally:
            if cursor:
                cursor.close()

            if con:
                con.close()




if __name__ == "__main__":
        main()



