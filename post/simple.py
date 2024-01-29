from tkinter import*
from PIL import Image,ImageTk
from customer import customer;
from postoffice import post;
from payment import op;
from services import services;
class simple:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Post office management system")
        #frame image
        img4=Image.open(r"images\p7.jpg")
        image4=img4.resize((1530,200))
        self.photo4=ImageTk.PhotoImage(img4)
        
        bg_lb=Label(self.root,image=self.photo4,bd=2,relief=RIDGE)
        bg_lb.place(x=0,y=0,width=1530,height=1000)
        
        lbl_title = Label(bg_lb, text="POST OFFICE MANAGEMENT", font=("times new roman", 37, "bold"), fg="red", bg="white")
        lbl_title.place(x=0,y=0,width=1600,height=100)
        
        
        #manage frame
        manage_frame=Frame(bg_lb,bd=1,relief=RIDGE,bg="white")
        manage_frame.place(x=0,y=160,width=1530,height=900)
        #button frame
        btn_frame=Frame(manage_frame,relief=RIDGE)
        btn_frame.place(x=10,y=5,width=1530,height=50)
        

        stud_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=35,font=("times new roman",14,"bold"),bg="red",fg="white",bd=0,cursor="hand2")
        stud_btn.grid(row=0,column=0)

        teach_btn=Button(btn_frame,text="POSTOFFICE",command=self.post_office_details,width=35,font=("times new roman",14,"bold"),bg="red",fg="white",bd=0,cursor="hand2")
        teach_btn.grid(row=0,column=1)

        sub_btn=Button(btn_frame,text="PAYMENT",command=self.op_details,width=35,font=("times new roman",14,"bold"),bg="red",fg="white",bd=0,cursor="hand2")
        sub_btn.grid(row=0,column=2)

        room_btn=Button(btn_frame,text="SERVICES",command=self.service_details,width=35,font=("times new roman",14,"bold"),bg="red",fg="white",bd=0,cursor="hand2")
        room_btn.grid(row=0,column=3)
        #bg image
        img2=Image.open(r"images\p7.jpg")
        img2=img2.resize((500,500),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img4)

        bg_lbl=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        bg_lbl.place(x=150,y=250,width=1200,height=600)

       

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=customer(self.new_window)

    def post_office_details(self):
        self.new_window=Toplevel(self.root)
        self.app=post(self.new_window)

    
    def op_details(self):
        self.new_window=Toplevel(self.root)
        self.app=op(self.new_window)

    
    def service_details(self):
        self.new_window=Toplevel(self.root)
        self.app=services(self.new_window)

    
    
 
    
 
       
                
if __name__ == "__main__":
    root=Tk()
    obj=simple(root)
    root.mainloop()

