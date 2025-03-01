from tkinter import *
from tkinter import Label
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk



top=Tk()
top.geometry('1500x700')
top.title("Login page")
#top.iconbitmap(r"C:\Users\Admin\Desktop\images 1.png")


path=r"C:\Users\Admin\Downloads\pawel-czerwinski-E68t7s48QA4-unsplash.jpg"
img=ImageTk.PhotoImage(Image.open(path))
l22=Label(top,image=img)
l22.pack()

def login():
    username = e1.get()
    password = e2.get()
    if username == "rishu" and password == "1234":
        top.destroy()
        import hotel 

    else:
        messagebox.showerror("Error", "Invalid username or password")

   


f = Frame(top, height=400, width=300, bg='black',relief=RIDGE)
f.place(x=500, y=200)

l1=Label(f,text='Username:', fg='white', bg='black', font=('Arial 15 bold'),bd=0)
l1.place(x=20,y=20)

e1=Entry(f, fg='red', font=('Arial 15 bold'))
e1.place(x=20,y=60)

l2=Label(f,text='Password:', fg='white', bg='black', font=('Arial 15 bold'),bd=0)
l2.place(x=20,y=100)

e2=Entry(f, fg='red', font=('Arial 15 bold'),show="*")
e2.place(x=20,y=140)

b1=Button(f,text='Login',font=('Arial 15 bold'),command=login)
b1.place(x=200,y=200)

b2=Button(f,text='New User Register',font=('Arial 10 bold'),bg='black',fg='white',bd=0)
b2.place(x=20,y=250)



def register_form():
    def register():
        username = e5.get()
        password = e6.get()
        confirm_password = e7.get()
        
        
        if password == confirm_password and username != "" and password != "":
            messagebox.showinfo("Success", "Registration successful")
        else:
            messagebox.showerror("Error", "Passwords do not match or fields are empty")




    f3 = Frame(top, height=400, width=300, bg='black', relief=RIDGE)
    f3.place(x=500, y=200)

    l4 = Label(f3,text='New Register Form', fg='white', bg='black', font=('Arial 20 bold'))
    l4.place(x=30, y=50)

    
    l5 = Label(f3, text='Username:', fg='white', bg='black', font=('Arial 15 bold'), bd=0)
    l5.place(x=20, y=100)

    e5 = Entry(f3, fg='red', font=('Arial 15 bold'))
    e5.place(x=20, y=140)

    l6 = Label(f3, text='Password:', fg='white', bg='black', font=('Arial 15 bold'), bd=0)
    l6.place(x=20, y=180)

    e6 = Entry(f3, fg='red', font=('Arial 15 bold'), show="*")
    e6.place(x=20, y=220)

    l7 = Label(f3, text='Confirm Password:', fg='white', bg='black', font=('Arial 15 bold'), bd=0)
    l7.place(x=20, y=260)

    e7 = Entry(f3, fg='red', font=('Arial 15 bold'), show="*")
    e7.place(x=20, y=300)

    # b4 = Button(f3, text='Register', font=('Arial 15 bold'), command=register)
    # b4.place(x=100, y=340)
    # b4 = Button(f3, text='Register', font=('Arial 15 bold'), command=lambda: [register(), f3.destroy(), login()])
    # b4.place(x=100, y=340)

    b4 = Button(f3, text='Register', font=('Arial 15 bold'), command=lambda: [register(), f3.destroy()])
    b4.place(x=100, y=340)






b2 = Button(f, text='New User Register', font=('Arial 10 bold'), bg='black', fg='white', bd=0, command=register_form)
b2.place(x=20, y=250)
#..........................forget
def forget_password():
    f4 = Frame(top, height=200, width=250, bg='black', relief=RIDGE)
    f4.place(x=500, y=300)

    l8 = Label(f4, text='Username/Email:', fg='white', bg='black', font=('Arial 15 bold'), bd=0)
    l8.place(x=20, y=20)

    e8 = Entry(f4, fg='red', font=('Arial 15 bold'))
    e8.place(x=20, y=60)

    


def forget_password():
    def send_password():
        username = e8.get()
        # Yahaan aap database se password fetch kar sakte hain
        password = "1234"
        messagebox.showinfo("Password", f"Your password is {password}")
        f4.destroy()
        login()

    f4 = Frame(top, height=200, width=250, bg='black', relief=RIDGE)
    f4.place(x=500, y=300)

    l8 = Label(f4, text='Username/Email:', fg='white', bg='black', font=('Arial 15 bold'), bd=0)
    l8.place(x=20, y=20)

    e8 = Entry(f4, fg='red', font=('Arial 15 bold'))
    e8.place(x=20, y=60)

    b5 = Button(f4, text='Send Password', font=('Arial 15 bold'), command=send_password)
    b5.place(x=50, y=120)




b3 = Button(f, text='Forget Password', font=('Arial 11 bold'), bg='black', fg='white', bd=0, command=forget_password)
b3.place(x=20, y=280)




top.mainloop()