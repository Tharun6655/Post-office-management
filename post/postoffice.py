from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class post:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Post office management system")
        
         #=============var===============
        self.var_office_id=StringVar()
        self.var_location=StringVar()
        self.var_manager_id=StringVar()
        self.var_operating_hours=StringVar()
        

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
        Dlf = LabelFrame(manage_frame, bd=4, relief=RIDGE, text="Postoffice Details",font=("times new roman", 12, "bold"), fg="red", bg="white")
        Dlf.place(x=10, y=200, width=660, height=400)

        # image1
        img2=Image.open(r"images\p8.jpeg")
        image2=img2.resize((400,400))
        self.photo2=ImageTk.PhotoImage(img2)
        
        bg_lb2=Label(self.root,image=self.photo2)
        bg_lb2.place(x=100,y=180,width=330,height=180)
       
        # post office information
         # office id
        office_id = Label(Dlf, font=("arial", 12, "bold"),text="Office_ID:")
        office_id.grid(row=3, column=1, sticky=W,padx=2,pady=7)

        lbl_office_id = ttk.Entry(Dlf,textvariable=self.var_office_id,font=("arial", 12, "bold"))
        lbl_office_id.grid(row=3, column=2,padx=2,pady=7)

        # location
        location = Label(Dlf, font=("arial", 12, "bold"),text="Location:")
        location.grid(row=4, column=1, sticky=W,padx=2,pady=7)

        lbl_loc = ttk.Entry(Dlf,textvariable=self.var_location ,font=("arial", 12, "bold"))
        lbl_loc.grid(row=4, column=2,padx=2,pady=7)

        # manager id
        lbl_mgrid = Label(Dlf, font=("times new roman", 12, "bold"), text="ManagerId:")
        lbl_mgrid.grid(row=5, column=1, sticky=W,padx=2,pady=7)

        ln_mgrid= ttk.Entry(Dlf,textvariable=self.var_manager_id,font=("times new roman", 12, "bold"))
        ln_mgrid.grid(row=5, column=2, sticky=W,padx=2,pady=7)

        #operating hours
        lbl_oprh = Label(Dlf, font=("times new roman", 12, "bold"), text="Operating hours:")
        lbl_oprh.grid(row=6, column=1, sticky=W,padx=2,pady=7)

        combo_oprh = ttk.Entry(Dlf,textvariable=self.var_operating_hours,font=("times new roman",12,"bold"))
        combo_oprh.grid(row=6, column=2, sticky=W,padx=2,pady=7)

       
        
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
        Drf = LabelFrame(manage_frame, bd=4, relief=RIDGE, text="Post Office Services",
                         font=("times new roman", 12, "bold"), fg="red", bg="white")
        Drf.place(x=680, y=10, width=850, height=600)
        
        
    
        
        
       # ===========table==================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Display",font=("times new roman",12,"bold"),bg="white",fg="red",padx=2)
        Table_Frame.place(x=690,y=200,width=860,height=450)

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=10,width=850,height=400)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.postoffice_Details_Table=ttk.Treeview(details_table,column=("office_id","location","manager_id","operating_hours"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.postoffice_Details_Table.xview)
        scroll_y.config(command=self.postoffice_Details_Table.yview)

        self.postoffice_Details_Table.heading("office_id",text="OfficeId")
        self.postoffice_Details_Table.heading("location",text="Location")
        self.postoffice_Details_Table.heading("manager_id",text="Manager_ID")
        self.postoffice_Details_Table.heading("operating_hours",text="operating_hours")
        
        self.postoffice_Details_Table["show"]="headings"
        self.postoffice_Details_Table.column("office_id",width=20)
        self.postoffice_Details_Table.column("location",width=20)
        self.postoffice_Details_Table.column("manager_id",width=20)
        self.postoffice_Details_Table.column("operating_hours",width=20)
        
        self.postoffice_Details_Table.pack(fill=BOTH,expand=1)
        self.postoffice_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_office_id.get()=="" or self.var_location.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into postoffice.branch values(%s,%s,%s,%s)",(
                                                                                self.var_office_id.get(),
                                                                                self.var_location.get(),
                                                                                self.var_manager_id.get(),
                                                                                self.var_operating_hours.get()
                                                                                
                                                                                
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","post office  details has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning","some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
        my_cursor=conn.cursor()
        my_cursor.execute("select * from branch")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.postoffice_Details_Table.delete(*self.postoffice_Details_Table.get_children())
            for i in rows:
                self.postoffice_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.postoffice_Details_Table.focus()
        content=self.postoffice_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_office_id.set(row[0]),
        self.var_location.set(row[1]),
        self.var_manager_id.set(row[2]),
        self.var_operating_hours.set(row[3]),
        
    
    def Update(self):
        if self.var_office_id.get()=="":
            messagebox.showerror("Error","Please enter appropriate data",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
                my_cursor=conn.cursor()
                my_cursor.execute("update postoffice.branch set location=%s, manager_id=%s, operating_hours=%s  where office_id=%s",(                                                                                                                                                          
                                                                                    
                                                                                    self.var_location.get(),
                                                                                    self.var_manager_id.get(),
                                                                                    self.var_operating_hours.get(),
                                                                                    self.var_office_id.get()
                                                                                    
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("update","post office details has been updated successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning","some thing went wrong:{str(es)}",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("PostOffice Management System","do you want delete post office details",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="postoffice")            
            my_cursor=conn.cursor()
            query="delete from branch where office_id=%s"
            value=(self.var_office_id.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        # conn.set("")

    def reset(self):
         self.var_office_id.set(""),
         self.var_location.set(""),
         self.var_manager_id.set(""),
         self.var_operating_hours.set(""),
         

if __name__ == "__main__":
    root = Tk()
    obj = post(root)
    root.mainloop()
