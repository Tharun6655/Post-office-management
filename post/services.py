from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class services:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Post office management system")
        
         #=============var===============
        self.var_pid=StringVar()
        self.var_sender_id=StringVar()
        self.var_receiver_id=StringVar()
        self.var_weight=StringVar()
        self.var_dimension=StringVar()
        self.var_amount=StringVar()
        self.var_status=StringVar()
        

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
        Dlf = LabelFrame(manage_frame, bd=4, relief=RIDGE, text="Track",font=("times new roman", 12, "bold"), fg="red", bg="white")
        Dlf.place(x=10, y=200, width=660, height=400)

        # image1
        img2=Image.open(r"images\p8.jpeg")
        image2=img2.resize((400,400))
        self.photo2=ImageTk.PhotoImage(img2)
        
        bg_lb2=Label(self.root,image=self.photo2)
        bg_lb2.place(x=100,y=180,width=330,height=180)
       
        # package information
         # package id
        p_id = Label(Dlf, font=("arial", 12, "bold"),text="P_ID:")
        p_id.grid(row=3, column=1, sticky=W,padx=2,pady=7)

        lbl_pid = ttk.Entry(Dlf,textvariable=self.var_pid,font=("arial", 12, "bold"))
        lbl_pid.grid(row=3, column=2,padx=2,pady=7)

        # sender
        sender_id = Label(Dlf, font=("arial", 12, "bold"),text="Sender_ID:")
        sender_id.grid(row=4, column=1, sticky=W,padx=2,pady=7)

        lbl_sender_id = ttk.Entry(Dlf,textvariable=self.var_sender_id ,font=("arial", 12, "bold"))
        lbl_sender_id.grid(row=4, column=2,padx=2,pady=7)

        # receiver id
        lbl_r_id = Label(Dlf, font=("times new roman", 12, "bold"), text="Receiver_Id:")
        lbl_r_id.grid(row=5, column=1, sticky=W,padx=2,pady=7)

        ln_rid= ttk.Entry(Dlf,textvariable=self.var_receiver_id,font=("times new roman", 12, "bold"))
        ln_rid.grid(row=5, column=2, sticky=W,padx=2,pady=7)

        #weight
        lbl_weight = Label(Dlf, font=("times new roman", 12, "bold"), text="Weight:")
        lbl_weight.grid(row=6, column=1, sticky=W,padx=2,pady=7)

        combo_weight = ttk.Entry(Dlf,textvariable=self.var_weight,font=("times new roman",12,"bold"))
        combo_weight.grid(row=6, column=2, sticky=W,padx=2,pady=7)
        #dimension
        lbl_dim = Label(Dlf, font=("times new roman", 12, "bold"), text="Dimension:")
        lbl_dim.grid(row=7, column=1, sticky=W,padx=2,pady=7)

        ln_rid= ttk.Entry(Dlf,textvariable=self.var_dimension,font=("times new roman", 12, "bold"))
        ln_rid.grid(row=7, column=2, sticky=W,padx=2,pady=7)
        #amount
        lbl_am = Label(Dlf, font=("times new roman", 12, "bold"), text="Amount:")
        lbl_am.grid(row=8, column=1, sticky=W,padx=2,pady=7)

        ln_am= ttk.Entry(Dlf,textvariable=self.var_amount,font=("times new roman", 12, "bold"))
        ln_am.grid(row=8, column=2, sticky=W,padx=2,pady=7)
        #status
        lbl_status = Label(Dlf, font=("times new roman", 12, "bold"), text="Status:")
        lbl_status.grid(row=9, column=1, sticky=W,padx=2,pady=7)

        ln_st= ttk.Entry(Dlf,textvariable=self.var_status,font=("times new roman", 12, "bold"))
        ln_st.grid(row=9, column=2, sticky=W,padx=2,pady=7)

       
        
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
        Drf = LabelFrame(manage_frame, bd=4, relief=RIDGE, text="Tracking",font=("times new roman", 12, "bold"), fg="red", bg="white")
        Drf.place(x=680, y=10, width=850, height=600)
        
        
    
        
        
       # ===========table==================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Display",font=("times new roman",12,"bold"),bg="white",fg="red",padx=2)
        Table_Frame.place(x=690,y=200,width=860,height=450)

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=10,width=850,height=400)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.service_Details_Table=ttk.Treeview(details_table,column=("pid","sender_id","receiver_id","weight","dimension","amount","status"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.service_Details_Table.xview)
        scroll_y.config(command=self.service_Details_Table.yview)

        self.service_Details_Table.heading("pid",text="PId")
        self.service_Details_Table.heading("sender_id",text="sender_id")
        self.service_Details_Table.heading("receiver_id",text="receiver_id")
        self.service_Details_Table.heading("weight",text="weight")
        self.service_Details_Table.heading("dimension",text="dimension")
        self.service_Details_Table.heading("amount",text="amount")
        self.service_Details_Table.heading("status",text="status")
        
        self.service_Details_Table["show"]="headings"
        self.service_Details_Table.column("pid",width=20)
        self.service_Details_Table.column("sender_id",width=20)
        self.service_Details_Table.column("receiver_id",width=20)
        self.service_Details_Table.column("weight",width=20)
        self.service_Details_Table.column("dimension",width=20)
        self.service_Details_Table.column("amount",width=20)
        self.service_Details_Table.column("status",width=20)
        
        self.service_Details_Table.pack(fill=BOTH,expand=1)
        self.service_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_pid.get()=="" or self.var_sender_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into postoffice.package values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_pid.get(),
                                                                                self.var_sender_id.get(),
                                                                                self.var_receiver_id.get(),
                                                                                self.var_weight.get(),
                                                                                self.var_dimension.get(),
                                                                                self.var_amount.get(),
                                                                                self.var_status.get()
                                                                                
                                                                                
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","package  details has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning","some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
        my_cursor=conn.cursor()
        my_cursor.execute("select * from postoffice.package")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.service_Details_Table.delete(*self.service_Details_Table.get_children())
            for i in rows:
                self.service_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.service_Details_Table.focus()
        content=self.service_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_pid.set(row[0]),
        self.var_sender_id.set(row[1]),
        self.var_receiver_id.set(row[2]),
        self.var_weight.set(row[3]),
        self.var_dimension.set(row[4]),
        self.var_amount.set(row[5]),
        self.var_status.set(row[6]),
        
    
    def Update(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Please enter appropriate data",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
                my_cursor=conn.cursor()
                my_cursor.execute("update postoffice.package set  sender_id=%s, receiver_id=%s, weight=%s, dimension=%s, amount=%s, status=%s where pid=%s",(                                                                                                                                                          
                                                                                
                                                                                self.var_sender_id.get(),
                                                                                self.var_receiver_id.get(),
                                                                                self.var_weight.get(),
                                                                                self.var_dimension.get(),
                                                                                self.var_amount.get(),
                                                                                self.var_status.get(),
                                                                                self.var_pid.get(),
                                                                                
                                                                                
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("update","package details has been updated successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning","some thing went wrong:{str(es)}",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("PostOffice Management System","do you want delete package details",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
            my_cursor=conn.cursor()
            query="delete from postoffice.package where pid=%s"
            value=(self.var_pid.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        # conn.set("")

    def reset(self):
         self.var_pid.set(""),
         self.var_sender_id.set(""),
         self.var_receiver_id.set(""),
         self.var_weight.set(""),
         self.var_dimension.set(""),
         self.var_amount.set(""),
         self.var_status.set(""),
         
         






if __name__ == "__main__":
    root = Tk()
    obj = services(root)
    root.mainloop()
