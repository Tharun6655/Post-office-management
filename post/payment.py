from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class op:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Post office management system")
        
         #=============var===============
        self.var_t_id=StringVar()
        self.var_pid=StringVar()
        self.var_eid=StringVar()
        self.var_date=StringVar()
        self.var_type=StringVar()
        

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
        Dlf = LabelFrame(manage_frame, bd=4, relief=RIDGE, text="Online Payment Details",font=("times new roman", 12, "bold"), fg="red", bg="white")
        Dlf.place(x=10, y=200, width=660, height=400)

        # image1
        img2=Image.open(r"images\p8.jpeg")
        image2=img2.resize((400,400))
        self.photo2=ImageTk.PhotoImage(img2)
        
        bg_lb2=Label(self.root,image=self.photo2)
        bg_lb2.place(x=100,y=180,width=330,height=180)
       
        # payment information
         # Transaction id
        t_id = Label(Dlf, font=("arial", 12, "bold"),text="T_ID:")
        t_id.grid(row=3, column=1, sticky=W,padx=2,pady=7)

        lbl_tid = ttk.Entry(Dlf,textvariable=self.var_t_id,font=("arial", 12, "bold"))
        lbl_tid.grid(row=3, column=2,padx=2,pady=7)

        # package id
        pid = Label(Dlf, font=("arial", 12, "bold"),text="P_ID:")
        pid.grid(row=4, column=1, sticky=W,padx=2,pady=7)

        lbl_pid = ttk.Entry(Dlf,textvariable=self.var_pid ,font=("arial", 12, "bold"))
        lbl_pid.grid(row=4, column=2,padx=2,pady=7)

        #employee id 
        lbl_eid = Label(Dlf, font=("times new roman", 12, "bold"), text="Emp_ID:")
        lbl_eid.grid(row=5, column=1, sticky=W,padx=2,pady=7)

        ln_eid = ttk.Entry(Dlf,textvariable=self.var_eid,font=("times new roman", 12, "bold"))
        ln_eid.grid(row=5, column=2, sticky=W,padx=2,pady=7)

        #date
        lbl_date = Label(Dlf, font=("times new roman", 12, "bold"), text="Date:")
        lbl_date.grid(row=6, column=1, sticky=W,padx=2,pady=7)

        combo_date = ttk.Entry(Dlf,textvariable=self.var_date,font=("times new roman",12,"bold"))
        combo_date.grid(row=6, column=2, sticky=W,padx=2,pady=7)

        # address
        lbl_type = Label(Dlf, font=("times new roman", 12, "bold"), text="Office_id:")
        lbl_type.grid(row=7, column=1, sticky=W,padx=2,pady=7)

        type_entry = ttk.Entry(Dlf,textvariable=self.var_type,font=("times new roman", 12, "bold"))
        type_entry.grid(row=7, column=2, sticky=W,padx=2,pady=7)

        
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
        Drf = LabelFrame(manage_frame, bd=4, relief=RIDGE, text="Payment Services",
                         font=("times new roman", 12, "bold"), fg="red", bg="white")
        Drf.place(x=680, y=10, width=850, height=600)
        
        
    
        
        
       # ===========table==================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Display",font=("times new roman",12,"bold"),bg="white",fg="red",padx=2)
        Table_Frame.place(x=690,y=200,width=860,height=450)

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=10,width=850,height=400)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.op_details=ttk.Treeview(details_table,column=("t_id","p_id","e_id","date","type"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.op_details.xview)
        scroll_y.config(command=self.op_details.yview)

        self.op_details.heading("t_id",text="T_ID")
        self.op_details.heading("p_id",text="P_ID")
        self.op_details.heading("e_id",text="E_ID")
        self.op_details.heading("date",text="Date")
        self.op_details.heading("type",text="Type")
        
        self.op_details["show"]="headings"
        self.op_details.column("t_id",width=20)
        self.op_details.column("p_id",width=20)
        self.op_details.column("e_id",width=20)
        self.op_details.column("date",width=20)
        self.op_details.column("type",width=20)
        self.op_details.pack(fill=BOTH,expand=1)
        self.op_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_t_id.get()=="" or self.var_pid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into postoffice.transaction values(%s,%s,%s,%s,%s)",(
                                                                                self.var_t_id.get(),
                                                                                self.var_pid.get(),
                                                                                self.var_eid.get(),
                                                                                self.var_date.get(),
                                                                                self.var_type.get(),
                                                                                
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","transaction details has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning","some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
        my_cursor=conn.cursor()
        my_cursor.execute("select * from transaction")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.op_details.delete(*self.op_details.get_children())
            for i in rows:
                self.op_details.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.op_details.focus()
        content=self.op_details.item(cursor_row)
        row=content["values"]

        self.var_t_id.set(row[0]),
        self.var_pid.set(row[1]),
        self.var_eid.set(row[2]),
        self.var_date.set(row[3]),
        self.var_type.set(row[4]),
        
    
    def Update(self):
        if self.var_t_id.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
            my_cursor=conn.cursor()
            my_cursor.execute("update postoffice.transaction set  p_id=%s, e_id=%s, date=%s, type=%s    where t_id=%s",(                                                                                                                                                          
                                                                                
                                                                                self.var_pid.get(),
                                                                                self.var_eid.get(),
                                                                                self.var_date.get(),
                                                                                self.var_type.get(),
                                                                                self.var_t_id.get()
                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","employee details has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("PostOffice Management System","do you want delete employee details",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
            my_cursor=conn.cursor()
            query="delete from transaction where t_id=%s"
            value=(self.var_t_id.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        # conn.set("")

    def reset(self):
         self.var_t_id.set(""),
         self.var_pid.set(""),
         self.var_eid.set(""),
         self.var_date.set(""),
         self.var_type.set(""),
         
        









if __name__ == "__main__":
    root = Tk()
    obj = op(root)
    root.mainloop()
