from tkinter import *
from PIL import Image, ImageTk




top = Tk()
top.geometry('1500x700')
top.title("hotel management")

f1 = LabelFrame(top, height=190, width=1500, bg='white')
f1.place(x=0, y=0)

def customer():
    top.destroy()
    import customer


def room():
    top.destroy()
    import room 


def detail():
    top.destroy()
    import detail
 
def logout():
    top.destroy()
    import login






path = r"C:\Users\Admin\OneDrive\Desktop\Images\image2.jpg"
img = Image.open(path)
img = img.resize((1500, 190))  # Resize image
img = ImageTk.PhotoImage(img)

l1 = Label(f1, image=img)
l1.place(x=0, y=0, width=1500, height=190)  # Adjust label size



path = r"C:\Users\Admin\OneDrive\Desktop\Images\images6.jpg"
img1 = Image.open(path)
img1.thumbnail((100, 100))  # Create thumbnail
img1 = ImageTk.PhotoImage(img1)

l2 = Label(f1, image=img1,relief=RIDGE)
l2.place(x=3, y=0)  # Left side par image


l3 = Label(top, text="HOTEL MANAGEMENT SYSTEM", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=4,relief=RIDGE)
l3.place(x=0, y=140, width=1550, height=50)

f2 = Frame(top, height=500, width=1500, bg='white',relief=RIDGE)
f2.place(x=0, y=191)

l4 = Label(top, text="MENU", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=4,relief=RIDGE)
l4.place(x=0, y=200, width=228,)

b1 = Frame(top,bd=4,relief=RIDGE)
b1.place(x=0,y=246,width=225,height=160)

# def customer():
#     top1 = Toplevel(top)
#     top1.title("customer")
#     top1.geometry('1139x450+230+240')

b2 = Button(top,text="CUSTOMER",width=18,height=2,font=("Arial 15 bold"),bg="black",fg="gold",cursor="hand1",command=customer)
b2.place(x=0,y=243,width=225,height=30)


b3 = Button(top,text="ROOM",width=18,height=2,font=("Arial 15 bold"),bg="black",fg="gold",cursor="hand1",command=room)
b3.place(x=0,y=275,width=225,height=30)

b4 = Button(top,text="DETAIL",width=18,height=2,font=("Arial 15 bold"),bg="black",fg="gold",cursor="hand1",command=detail)
b4.place(x=0,y=308,width=225,height=30)

#b5 = Button(top,text="REPORT",width=18,height=2,font=("Arial 15 bold"),bg="black",fg="gold",cursor="hand1",command=report)
#b5.place(x=0,y=340,width=225,height=30)

b6 = Button(top,text="LOGOUT",width=18,height=2,font=("Arial 15 bold"),bg="black",fg="gold",cursor="hand1",command=logout)
b6.place(x=0,y=340,width=225,height=30)


path = r"C:\Users\Admin\OneDrive\Desktop\Images\istockphoto-1333257950-612x612.jpg"
img2 = Image.open(path)
img2 = img2.resize((1300, 500))  # Resize image
img2 = ImageTk.PhotoImage(img2)

l5 = Label(f2, image=img2)
l5.place(x=225, y=0, width=1300, height=500)  # Adjust label size

path = r"C:\Users\Admin\OneDrive\Desktop\Images\WhatsApp Image 2025-01-12 at 02.53.34_5da471a0.jpg"
img3 = Image.open(path)
img3 = img3.resize((226, 250))  # Resize image
img3 = ImageTk.PhotoImage(img3)

l6 = Label(f2, image=img3)
l6.place(x=0, y=200, width=226, height=250)  # Adjust label size



top.mainloop()
