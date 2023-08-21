from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
import time
import os
import tempfile

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title(" Student Management System version 0.7 | Developed by Vinod")
        self.root.geometry("1350x700+0+0")
        

        #self.icon_title=PhotoImage(file=r"C:\Users\ram\Desktop\LMS\NicePng_student-png_81754.png")
        
        title=Label(self.root,text="         STUDENT MANAGEMENT SYSTEM",font=("times new roman",22,"bold" ),fg="white",bg="#010c48",relief=GROOVE,bd=5)
        title.pack(side=TOP,fill=X)

        self.lbl_clock=Label(self.root,text="WELCOME TO S.M.S\t\t Date :DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",16,),bg="lightgrey",fg="black",bd=3,relief=GROOVE)
        self.lbl_clock.place(x=0,y=43,relwidth=1,height=27)
        
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.mobile_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
 #========================Left Frame =================================================
        
        Manage_frame=Frame(self.root,bd=5,relief=GROOVE,bg="lightgrey")
        Manage_frame.place(x=5,y=68,width=450,height=620)
        
        img=Image.open(r"C:\Users\ram\Downloads\education-png-23451.png")
        img=img.resize((100,70),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img)

        lbl_img=Label(Manage_frame,image=self.photoimg2,bg="lightgrey")
        lbl_img.place(x=0,y=20,width=100,height=70)
        
        
        lbl_Std1=Label(Manage_frame,text="  Manage Students ",font=("times new roman",28,"bold"),bg="lightgrey").place(x=100,y=40)

        lbl_roll=Label(Manage_frame,text="Roll No",font=("times new roman",20),bg="lightgrey")
        lbl_roll.place(x=20,y=130)
        ent_roll=Entry(Manage_frame,textvariable=self.roll_no_var,font=("times new roman",16),bg="white",bd=2)
        ent_roll.place(x=160,y=135)

        lbl_name=Label(Manage_frame,text="Name",font=("times new roman",20),bg="lightgrey")
        lbl_name.place(x=20,y=180)
        ent_name=Entry(Manage_frame,textvariable=self.name_var,font=("times new roman",16),bg="white",bd=2)
        ent_name.place(x=160,y=185)

        
        lbl_email=Label(Manage_frame,text="Email Id",font=("times new roman",20),bg="lightgrey")
        lbl_email.place(x=20,y=230)
        ent_email=Entry(Manage_frame,textvariable=self.email_var,font=("times new roman",16 ),bg="white",bd=2)
        ent_email.place(x=160,y=235)
        
        lbl_gender=Label(Manage_frame,text="Gender",font=("times new roman",20 ),bg="lightgrey")
        lbl_gender.place(x=20,y=280)
        
        combo_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=("times new roman",15 ))
        combo_gender["values"]=("Male"," Female","Other")
        combo_gender.place(x=160,y=285)
        
        lbl_contact_no=Label(Manage_frame,text="Mobile",font=("times new roman",20 ),bg="lightgrey")
        lbl_contact_no.place(x=20,y=330)
        
        ent_contact_no=Entry(Manage_frame,textvariable=self.mobile_var,font=("times new roman",16 ),bg="white",bd=2)
        ent_contact_no.place(x=160,y=335)

        lbl_dob=Label(Manage_frame,text="D.O.B",font=("times new roman",18 ),bg="lightgrey")
        lbl_dob.place(x=20,y=390)
        ent_dob=Entry(Manage_frame,textvariable=self.dob_var,font=("times new roman",16 ),bg="white",bd=2)
        ent_dob.place(x=160,y=395)

        lbl_address=Label(Manage_frame,text="Address",font=("times new roman",20 ),bg="lightgrey")
        lbl_address.place(x=20,y=440)
        self.ent_address=Text(Manage_frame,font=("times new roman",16 ),bg="white",bd=2)
        self.ent_address.place(x=160,y=445,width=228,height=95)
        
        
    #========================Left Frame Button =================================================
        
        
        btn_frame=Frame(Manage_frame,bd=5,relief=RIDGE,bg="lightgrey")
        btn_frame.place(x=2,y=547,width=435,height=60)
        
        
        btn_add=Button(Manage_frame,command=self.add_student,text="Add",font=("gloudy old style",13),bd=3,bg="#008080",fg="white")
        btn_add.place(x=10,y=560,width=100)

        btn_update=Button(Manage_frame,command=self.update,text="Update",font=("gloudy old style",13),bd=3,bg="#8B5A2B",fg="white")
        btn_update.place(x=115,y=560,width=100)

        btn_delete=Button(Manage_frame,command=self.delete,text="Delete",font=("gloudy old style",13),bd=3,bg="#308014",fg="white")
        btn_delete.place(x=220,y=560,width=100)

        btn_clear=Button(Manage_frame,command=self.clear,text="Clear",font=("gloudy old style",13),bd=3,bg="#CD3278",fg="white")
        btn_clear.place(x=325,y=560,width=100)


#======================== Right Frame =================================================
        
        Sudent_detail_frame=Label(self.root,bd=5,relief=RIDGE,bg="lightgrey")
        Sudent_detail_frame.place(x=470,y=68,width=800,height=620)

        img=Image.open(r"C:\Users\ram\Downloads\Child-Student-PNG-Free-Image.png")
        img=img.resize((630,330),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(Sudent_detail_frame,image=self.photoimg,bd=10,relief=GROOVE)
        lbl_img.place(x=9,y=330,width=770,height=280)

        lbl_search=Label(Sudent_detail_frame,text="Search By",font=("times new roman",20 ),bg="lightgrey")
        lbl_search.place(x=30,y=40)
        
        combo_search=ttk.Combobox(Sudent_detail_frame,textvariable=self.search_by,font=("times new roman",14 ))
        combo_search["values"]=("Name"," Mobile","Roll")
        combo_search.place(x=170,y=42)


        txt_search=Entry(Sudent_detail_frame,textvariable=self.search_txt,font=("times new roman",14 ),bg="white",bd=2)
        txt_search.place(x=390,y=42)

        search=Button(Sudent_detail_frame,command=self.search_data,text="Search",font=("gloudy old style",13),bd=3,bg="#BDFCC9",fg="black")
        search.place(x=590,y=40,width=80)

        btn_show=Button(Sudent_detail_frame,command=self.fetch_data,text="Show all",font=("gloudy old style",13),bd=3,bg="#EEE9E9",fg="black")
        btn_show.place(x=690,y=40,width=80)

        self.update_date_time()
        
#======================== Table Frame =================================================

        
        table_frame=Frame(Sudent_detail_frame,bd=5,relief=RIDGE,bg="lightgrey")
        table_frame.place(x=10,y=80,width=770,height=250)

        
        

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","mobile","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email ID")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("mobile",text="Mobile")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        self.Student_table["show"]="headings"
        self.Student_table.column("roll",width=70)
        self.Student_table.column("name",width=120)
        self.Student_table.column("email",width=150)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("mobile",width=90)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("address",width=340)
        self.Student_table.pack()
        self.Student_table.bind("<ButtonRelease-1>",self.get_data)
        self.fetch_data()       

    def add_student(self):
        if self.roll_no_var.get()=="":
            messagebox.showerror("Error","Fill  Student Roll No ")
        
        elif self.name_var.get()=="":
            messagebox.showerror("Error","Fill  Student Name ")
        
        elif self.email_var.get()=="":
            messagebox.showerror("Error","Fill  Email ID  ")
        
        
        elif self.gender_var.get()=="":
            messagebox.showerror("Error","Select Gender ")


        elif self.mobile_var.get()=="":
            messagebox.showerror("Error","Enter Mobile Number ")

        elif self.dob_var.get()=="":
            messagebox.showerror("Error","Enter Date of Birth ")
        
        elif self.roll_no_var.get()=="roll":
            messagebox.showerror("Error","Roll no Alreday Exits ")
        
        
        
        
        else:
        
            con=mysql.connector.connect(host="localhost",user="root",password="Vin@deep534",database="om")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.roll_no_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.mobile_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.ent_address.get("1.0",END)
                                                                            ))
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo(" Success","Data Save Successfully")


    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="Vin@deep534",database="om")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()

        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("",END,values=row)
                con.commit()
        
        con.close()
                
    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.mobile_var.set("")
        self.dob_var.set("")
        self.search_by.set("")
        self.search_txt.set("")
        self.ent_address.delete("1.0",END)
        
    def get_data(self,ev):
        f=self.Student_table.focus()
        content=self.Student_table.item(f)
        row=content["values"]
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.mobile_var.set(row[4])
        self.dob_var.set(row[5]) 
        self.ent_address.delete('1.0',END)
        self.ent_address.insert(END,row[6])    

    def update(self):
        con=mysql.connector.connect(host="localhost",user="root",password="Vin@deep534",database="om")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,mobile=%s,dob=%s,address=%s where roll=%s ",(
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.mobile_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.ent_address.get("1.0",END),
                                                                            self.roll_no_var.get(),
                                                                            ))
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo(" Success","Data Updated Successfully")


    def delete(self):
        if self.roll_no_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:    
            con=mysql.connector.connect(host="localhost",user="root",password="Vin@deep534",database="om")
            cur=con.cursor()
            query="delete from students where roll=%s"
            value=(self.roll_no_var.get(),)
            cur.execute(query,value)
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo(" Delete","Data Delete Successfully")



    def search_data(self):
        if self.search_by.get()=="":
            messagebox.showerror("Error","First Select the Option")
        else:    
            con=mysql.connector.connect(host="localhost",user="root",password="Vin@deep534",database="om")
            cur=con.cursor()
            cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert("",END,values=row)
                    con.commit()
            
            con.close()
    
        
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")

        self.lbl_clock.config(text=f"WELCOME TO S.M.S\t\t Date :  {str(date_)}\t\t Time :  {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)   





root=Tk()
root.title('Clock')
obj=Student(root)
root.mainloop()
