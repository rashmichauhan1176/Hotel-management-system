from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql as sql
from time import strftime
from datetime import datetime


top = Tk()
top.geometry('1139x550+230+150')
top.title("hotel management")

l = Label(top, text="ROOMBOOKING DETAIL", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=3,relief=RIDGE)
l.place(x=0, y=0, width=1130, height=50)


path = r"C:\Users\Admin\OneDrive\Desktop\Images\images6.jpg"
img1 = Image.open(path)
img1.thumbnail((50, 45))  # Create thumbnail
img1 = ImageTk.PhotoImage(img1)

l2 = Label(top, image=img1,relief=RIDGE)
l2.place(x=2, y=0)  # Left side par image
#.....................Laber frame....................................................
l1 = LabelFrame(top,bd=2,relief=RIDGE,text="New Room Add",font=("Arial 12 bold"),padx=2)
l1.place(x=5,y=50,width=480,height=350)

#............................Floor.....................................
l2 = Label(l1,text="Floor",font=("Arial 12 bold"),padx=2,pady=6)
l2.grid(row=0,column=0,sticky=W)

top.var_floor=StringVar()

e1 = ttk.Entry(l1,width=23,textvariable=top.var_floor,font=("Arial 13 bold"))
e1.grid(row=0,column=1,sticky=W)

#.......................................................
l3 = Label(l1,text="Room No",font=("Arial 12 bold"),padx=2,pady=6)
l3.grid(row=1,column=0,sticky=W)

top.var_room_no=StringVar()

e2 = ttk.Entry(l1,width=23,textvariable=top.var_room_no,font=("Arial 13 bold"))
e2.grid(row=1,column=1,sticky=W)
#........................................................................
l4 = Label(l1,text="Room Type",font=("Arial 12 bold"),padx=2,pady=6)
l4.grid(row=2,column=0,sticky=W)

top.var_room_type=StringVar()

e3 = ttk.Entry(l1,width=23,textvariable=top.var_room_type,font=("Arial 13 bold"))
e3.grid(row=2,column=1,sticky=W)

#.............................................................
def add():
    floor = e1.get()
    room_no = e2.get()
    room_type = e3.get()
    
    
    if not all([floor,room_no,room_type,]):
        messagebox.showerror("Error","please fill all fields")
        return
    
    try:
        db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
        cur = db.cursor()
        query=("INSERT INTO detail (floor, room_no, room_type) VALUES (%s, %s, %s)")
        value=(floor, room_no, room_type)
        cur.execute(query,value)
        db.commit()
        if cur.rowcount > 0:
            messagebox.showinfo("Success", "Record inserted successfully")
            e1.delete(0,"end")
            e2.delete(0,"end")
            e3.delete(0,"end")
            

        else:
            messagebox.showerror("Error", "Record not inserted")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        tv.fetch_data()
        db.close()

#............................fetch data....................................
def fetch_data():
    tv.delete(*tv.get_children())
    db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
    cur = db.cursor()
    cur.execute("select * from detail")
    rows=cur.fetchall()
    if len(rows)!=0:
        for row in rows:
            tv.insert("",END,values=row)
    db.commit()
    db.close()


#....................get cursor................................................
def get_cursor(tv, event):
    cursor_row = tv.focus()
    content = tv.item(cursor_row)
    row = content["values"]
    top.var_floor.set(row[0])
    top.var_room_no.set(row[1])
    top.var_room_type.set(row[2])

#...........................update.........................................
def update():
    floor = e1.get()
    room_no = e2.get()
    room_type = e3.get()
    try:
        db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
        cur = db.cursor()
        cur.execute("update detail set room_no=%s, room_type=%s where floor=%s", (room_no, room_type, floor))
        db.commit()
        if cur.rowcount > 0:
            messagebox.showinfo('result', 'record updated successfully')
            e1.delete(0, "end")
            e2.delete(0, "end")
            e3.delete(0, "end")
        else:
            messagebox.showinfo('result', 'record not updated')
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        db.close()

#........................delete........................
def delete():
    floor = e1.get()
    try:
        db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
        cur = db.cursor()
        cur.execute("delete from detail where floor=%s", (floor,))
        db.commit()
        if cur.rowcount > 0:
            messagebox.showinfo('result', 'record deleted successfully')
            e1.delete(0, "end")
            e2.delete(0, "end")
            e3.delete(0, "end")
        else:
            messagebox.showinfo('result', 'record not found')
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        db.close()
        fetch_data()  # Delete ke baad fetch_data ko call karein

#...................reset...................................

def reset():
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    top.var_floor.set("")
    top.var_room_no.set("")
    top.var_room_type.set("")








#......................btn..........................
f1 = Frame(l1,bd=2,relief=RIDGE)
f1.place(x=0,y=200,width=365,height=40)

b3 = Button(f1,text="Add",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=add)
b3.grid(row=0,column=0)

b4 = Button(f1,text="Update",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=update)
b4.grid(row=0,column=1)

b5 = Button(f1,text="Delete",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=delete)
b5.grid(row=0,column=2)

b6 = Button(f1,text="Reset",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=reset)
b6.grid(row=0,column=3)

b7 = Button(f1,text="Fetch Data",font=("Arial 13 bold"),bg='black',fg='gold',width=10,command=fetch_data)
b7.grid(row=0,column=4)



#...................right side frame...............................
l5 = LabelFrame(top,bd=2,relief=RIDGE,text="show room detail",font=("Arial 12 bold"),padx=2)
l5.place(x=550,y=50,width=575,height=350)

#.....................scroll bar..................................
scroll_x = ttk.Scrollbar(l5,orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(l5,orient=VERTICAL)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)



tv = ttk.Treeview(l5,selectmode="browse",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=tv.xview)
scroll_y.config(command=tv.yview)
tv['columns']=( 'Floor','Room_no','Room_type')

tv.column('#0', width=0, stretch=NO)
for col in tv['columns']:
    tv.column(col,anchor=CENTER,width=100)
    for col in tv['column']:
        tv.heading(col,text=col,anchor=CENTER)
tv.column('Floor', anchor=CENTER, width=110)
tv.column('Room_no', anchor=CENTER, width=100)
tv.column('Room_type', anchor=CENTER, width=100)

tv["show"]="headings"

tv.heading('Floor', text='Floor', anchor=CENTER)
tv.heading('Room_no', text='Room_no', anchor=CENTER)
tv.heading('Room_type', text='Room_type', anchor=CENTER)


tv.fetch_data = fetch_data  # Method ko define karein
tv.pack(fill=BOTH,expand=1)
tv.fetch_data()  # Method ko call karein
tv.bind("<ButtonRelease-1>", lambda event: get_cursor(tv, event))











top.mainloop()