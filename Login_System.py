from tkinter import *
from tkinter import messagebox

class Login :
    def __init__(self,window):
        self.window=window
        self.window.title("Login System")
        self.window.geometry("800x600")
        self.window.config(background="#FF3300")
        login_frame=Frame(window,width=500,height=340,bg="white")
        title=Label(login_frame,text="Login Here : ",font=("Impact",35,"bold"),bg="white",fg="#FF3300").place(x=90,y=30)
        title2=Label(login_frame, text="Accountant Employee Login Area ", font=("Goudy old style", 15, "bold"), bg="white", fg="#FF3300").place(x=90, y=90)
        Username = Label(login_frame, text="Username : ", font=("times new roman", 15), bg="white", fg="grey").place(x=90, y=120)
        self.Username_entry=Entry(login_frame,bg="lightgrey",width=50).place(x=90,y=150,height=35)
        Password = Label(login_frame, text="Password : ", font=("times new roman", 15), bg="white", fg="grey").place(x=90, y=190)
        self.Password_entry = Entry(login_frame, bg="lightgrey", width=50).place(x=90, y=220, height=35)
        Forget=Button(login_frame,text="Forget Password ?",bg="white",fg="#FF3300",bd=0,font=("times new roman", 12)).place(x=90,y=260)
        Login_button = Button(self.window,command=self.Login_code, text="Login", fg="white", bg="#FF3300",width=30,font=("times new roman", 12)).place(x=250, y=450)
        login_frame.pack(expand=YES)
    def Login_code(self):
        if self.Username_entry ==" " or self.Password_entry==" " :
            messagebox.showerror("Error","All Fields Are Required !",parent=self.window)
        elif self.Username_entry!="reda"or self.Password_entry.get()!="12345" :
            messagebox.showerror("Error","Invalid Username/Password",parent=self.window)
        else:
            messagebox.showerror("Welcome",f"Welcome {self.Username_entry}\n Your Password : {self.Password_entry}", parent=self.window)


window=Tk()
obj=Login(window)
window.mainloop()
