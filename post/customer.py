from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class customer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Post office management system")
        
         #=============var===============
        self.var_cust_id=StringVar()
        self.var_fn=StringVar()
        self.var_ln=StringVar()
        self.var_gn=StringVar()
        self.var_add=StringVar()
        self.var_ph=StringVar()
        self.var_em=StringVar()
        

        # bg image
        img4 = Image.open(r"images\p7.jpg")
        image4 = img4.resize((1530, 200))
        self.photo4 = ImageTk.PhotoImage(img4)

        bg_lb = Label(self.root, image=self.photo4, bd=2, relief=RIDGE)
        bg_lb.place(x=0, y=0, width=1530, height=1000)

        lbl_title = Label(bg_lb, text="POST OFFICE MANAGEMENT", font=("times new roman", 37, "bold"), fg="red", bg="white")
        lbl_title.place(x=0, y=0, width=1600, height=100)

        # manage frame
        manage_frame = Frame(bg_lb, bd=1, relief=RIDGE, bg="white")
        manage_frame.place(x=0, y=160, width=1530, height=900)

        # left frame
        Dlf = LabelFrame(manage_frame, bd=4, relief=RIDGE, text="Customer Details",font=("times new roman", 12, "bold"), fg="red", bg="white")
        Dlf.place(x=10, y=200, width=660, height=400)

        # image1
        img2=Image.open(r"images\p8.jpeg")
        image2=img2.resize((400,400))
        self.photo2=ImageTk.PhotoImage(img2)
        
        bg_lb2=Label(self.root,image=self.photo2)
        bg_lb2.place(x=100,y=180,width=330,height=180)
       
        # customer information
         # customer fname
        cust_id = Label(Dlf, font=("arial", 12, "bold"),text="Cust ID:")
        cust_id.grid(row=3, column=1, sticky=W,padx=2,pady=7)

        lbl_fn = ttk.Entry(Dlf,textvariable=self.var_cust_id,font=("arial", 12, "bold"))
        lbl_fn.grid(row=3, column=2,padx=2,pady=7)

        # customer fname
        fname = Label(Dlf, font=("arial", 12, "bold"),text="First Name:")
        fname.grid(row=4, column=1, sticky=W,padx=2,pady=7)

        lbl_fn = ttk.Entry(Dlf,textvariable=self.var_fn ,font=("arial", 12, "bold"))
        lbl_fn.grid(row=4, column=2,padx=2,pady=7)

        # lastname
        lbl_ln = Label(Dlf, font=("times new roman", 12, "bold"), text="Last Name:")
        lbl_ln.grid(row=5, column=1, sticky=W,padx=2,pady=7)

        ln_entry = ttk.Entry(Dlf,textvariable=self.var_ln,font=("times new roman", 12, "bold"))
        ln_entry.grid(row=5, column=2, sticky=W,padx=2,pady=7)

        #gender
        lbl_gen = Label(Dlf, font=("times new roman", 12, "bold"), text="Gender:")
        lbl_gen.grid(row=6, column=1, sticky=W,padx=2,pady=7)

        combo_gn = ttk.Entry(Dlf,textvariable=self.var_gn,font=("times new roman",12,"bold"))
        combo_gn.grid(row=6, column=2, sticky=W,padx=2,pady=7)

        # address
        lbl_add = Label(Dlf, font=("times new roman", 12, "bold"), text="Address:")
        lbl_add.grid(row=7, column=1, sticky=W,padx=2,pady=7)

        add_entry = ttk.Entry(Dlf,textvariable=self.var_add,font=("times new roman", 12, "bold"))
        add_entry.grid(row=7, column=2, sticky=W,padx=2,pady=7)

        # phone number
        lbl_ph = Label(Dlf, font=("times new roman", 12, "bold"), text="Phone No:")
        lbl_ph.grid(row=8, column=1, sticky=W,padx=2,pady=7)

        ph_entry = ttk.Entry(Dlf,textvariable=self.var_ph,font=("times new roman", 12, "bold"))
        ph_entry.grid(row=8, column=2, sticky=W,padx=2,pady=7)

        # email
        lbl_em = Label(Dlf, font=("times new roman", 12, "bold"), text="Email-ID:")
        lbl_em.grid(row=9, column=1, sticky=W,padx=2,pady=7)

        em_entry = ttk.Entry(Dlf,textvariable=self.var_em,font=("times new roman", 12, "bold"))
        em_entry.grid(row=9, column=2, sticky=W,padx=2,pady=7)

                # ---------------------btn---------------------------
        btn_frame=Frame(Dlf,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="red",fg="white",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.Update,font=("arial",12,"bold"),bg="red",fg="white",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="red",fg="white",width=9)
        btnReset.grid(row=0,column=2,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="red",fg="white",width=9)
        btnDelete.grid(row=0,column=3,padx=1)



        
        
        # right frame
        Drf = LabelFrame(manage_frame, bd=4, relief=RIDGE, text="Customer details",
                         font=("times new roman", 12, "bold"), fg="red", bg="white")
        Drf.place(x=680, y=10, width=850, height=600)
        
        
    
        
        
       # ===========table==================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Display",font=("times new roman",12,"bold"),bg="white",fg="red",padx=2)
        Table_Frame.place(x=690,y=200,width=860,height=450)

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=10,width=850,height=400)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("cust_id","firstname","lastname","gender","address","email","phonenumber"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("cust_id",text="customerId")
        self.Cust_Details_Table.heading("firstname",text="FirstName")
        self.Cust_Details_Table.heading("lastname",text="LastName")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("address",text="Address")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("phonenumber",text="PhoneNumber")
        
        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.column("cust_id",width=20)
        self.Cust_Details_Table.column("firstname",width=20)
        self.Cust_Details_Table.column("lastname",width=20)
        self.Cust_Details_Table.column("gender",width=20)
        self.Cust_Details_Table.column("email",width=20)
        self.Cust_Details_Table.column("phonenumber",width=20)
        

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_fn.get()=="" or self.var_ln.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_cust_id.get(),
                                                                                self.var_fn.get(),
                                                                                self.var_ln.get(),
                                                                                self.var_gn.get(),
                                                                                self.var_add.get(),
                                                                                self.var_em.get(),
                                                                                self.var_ph.get(),
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning","some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_cust_id.set(row[0]),
        self.var_fn.set(row[1]),
        self.var_ln.set(row[2]),
        self.var_gn.set(row[3]),
        self.var_add.set(row[4]),
        self.var_em.set(row[5]),
        self.var_ph.set(row[6]),
        
    
    def Update(self):
        if self.var_fn.get()=="":
            messagebox.showerror("Error","Please enter appropriate details",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
            my_cursor=conn.cursor()
            my_cursor.execute("update postoffice.customer set  firstname=%s, lastname=%s, gender=%s, address=%s, email=%s, phonenumber=%s  where cust_id=%s",(                                                                                                                                                          
                                                                                
                                                                                self.var_fn.get(),
                                                                                self.var_ln.get(),
                                                                                self.var_gn.get(),
                                                                                self.var_add.get(),
                                                                                self.var_em.get(),
                                                                                self.var_ph.get(),
                                                                                self.var_cust_id.get()
                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","customer details has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("PostOffice Management System","do you want delete customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
            my_cursor=conn.cursor()
            query="delete from customer where cust_id=%s"
            value=(self.var_cust_id.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        # conn.set("")

    def reset(self):
         self.var_cust_id.set(""),
         self.var_fn.set(""),
         self.var_ln.set(""),
         self.var_gn.set(""),
         self.var_add.set(""),
         self.var_em.set(""),
         self.var_ph.set(""),
         
        
    def Search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
        my_cursor=conn.cursor()

        my_cursor.execute("Select * from customer where " + str(self.Search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")




        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()









if __name__ == "__main__":
    root = Tk()
    obj = customer(root)
    root.mainloop()
