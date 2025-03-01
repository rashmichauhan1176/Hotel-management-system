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


#...............Variables.........................................................
top.var_contact = StringVar()
top.var_checkin = StringVar()
top.var_checkout = StringVar()
top.var_roomtype = StringVar()
top.var_available_room = StringVar()
top.var_meal = StringVar()
top.var_noofdays = StringVar()
top.var_paidtax = StringVar()
top.var_subtotal = StringVar()
top.var_total = StringVar()

top.var_available = StringVar()

db = sql.connect(host='localhost', user='root', password='rishu123', db='project3')
cur = db.cursor()


#......................add...............................................
def add():
    contact = e1.get()
    check_in = e2.get()
    check_out = e3.get()
    room_type = e4.get()
    available_room = e5.get()
    meal = e6.get()
    no_of_days = e7.get()
    
    if not all([contact,check_in,check_out,room_type,available_room,meal,no_of_days]):
        messagebox.showerror("Error","please fill all fields")
        return
    
    try:
        db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
        cur = db.cursor()
        query=("INSERT INTO room (contact, check_in, check_out, room_type, available_room, meal, no_of_days) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        value=(contact, check_in, check_out, room_type, available_room, meal, no_of_days)
        cur.execute(query,value)
        db.commit()
        if cur.rowcount > 0:
            messagebox.showinfo("Success", "Record inserted successfully")
            e1.delete(0,"end")
            e2.delete(0,"end")
            e3.delete(0,"end")
            e4.delete(0, END)
            e5.delete(0,"end")
            e6.delete(0,"end")
            e7.delete(0,"end")
            e8.delete(0, END)
            e9.delete(0, END)
            e10.delete(0,"end")

        else:
            messagebox.showerror("Error", "Record not inserted")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        db.close()

#..........................update..................................
def update():
    contact = e1.get()
    check_in = e2.get()
    check_out = e3.get()
    room_type = e4.get()
    available_room = e5.get()
    meal = e6.get()
    no_of_days = e7.get()
    cur.execute("update room set check_in=%s, check_out=%s, room_type=%s, available_room=%s, meal=%s, no_of_days=%s where contact=%s", (check_in, check_out, room_type, available_room, meal, no_of_days, contact))
    db.commit()
    if cur.rowcount > 0:
        messagebox.showinfo('result', 'record updated successfully')
        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.set("")
        e5.delete(0, "end")
        e6.set("")
        e7.delete(0, "end")
    else:
        messagebox.showinfo('result', 'record not updated')

#......................Delete................................................
def delete():
    contact = e1.get()
    global db
    try:
        cur = db.cursor()
        cur.execute("delete from room where contact=%s", (contact,))
        db.commit()
        if cur.rowcount > 0:
            messagebox.showinfo('result', 'record deleted successfully')
            e1.delete(0, "end")
            e2.delete(0, "end")
            e3.delete(0, "end")
            e4.set("")
            e5.delete(0, "end")
            e6.set("")
            e7.delete(0, "end")
            e8.set("")
            e9.set("")
            e10.delete(0, "end")
        else:
            messagebox.showinfo('result', 'record not deleted')
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        pass

#........................search..........................................
def search():
    x = e12.get()
    if x == "Contact":
        query = "select * from customers where contact = %s"
        value = (e13.get(),)
        cur.execute(query, value)
        result = cur.fetchall()
        tv.delete(*tv.get_children())
        for row in result:
            tv.insert("", 'end', values=row)
    elif x == "Available_Room":
        query = "select * from room where available_room = %s"
        value = (e13.get(),)
        cur.execute(query, value)
        result = cur.fetchall()
        tv.delete(*tv.get_children())
        for row in result:
            tv.insert("", 'end', values=row)
    else:
        messagebox.showerror("Error", "Please select a valid option")







#.........................Reset........................................
def reset():
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.set("")
    e5.delete(0, "end")
    e6.set("")
    e7.delete(0, "end")
    e8.delete(0, "end")
    e9.delete(0, "end")
    e10.delete(0, "end")
    for widget in f4.winfo_children():
        widget.destroy()

#.......................show...................................
def show():
    for i in tv.get_children():
        tv.delete(i)
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='rishu123', db='project3')
    cur = db.cursor()
    query = "select * from room"
    cur.execute(query)
    rows = cur.fetchall()
    if cur.rowcount > 0:
        for col in rows:
            contact = col[0]
            check_in = col[1]
            check_out = col[2]
            room_type = col[3]
            available_room = col[4]
            meal = col[5]
            no_of_days = col[6]
            tv.insert("", 'end', values=(contact, check_in, check_out, room_type, available_room, meal, no_of_days))
    else:
        messagebox.showinfo("result", "record not found")


#........................fetch data.................................
def fetch_data():
    tv.delete(*tv.get_children())
    db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
    cur = db.cursor()
    cur.execute("select * from room")
    rows=cur.fetchall()
    if len(rows)!=0:
        for row in rows:
            tv.insert("",END,values=row)
    db.commit()
    db.close()

#...........................get cursor...................................................................
def get_cursor(tv, event):
    cursor_row = tv.focus()
    content = tv.item(cursor_row)
    row = content["values"]
    if row:  
        try:
            top.var_contact.set(row[0])
            top.var_checkin.set(row[1])
            top.var_checkout.set(row[2])
            top.var_roomtype.set(row[3])
            top.var_available.set(row[4])
            top.var_meal.set(row[5])
            top.var_noofdays.set(row[6])
            top.var_paidtax.set(row[7])
            top.var_subtotal.set(row[8])
            top.var_total.set(row[9])
        except Exception as e:
            messagebox.showerror("Error", str(e))


#...............................Bill.........................................................................
def total():
    inDate = top.var_checkin.get()
    outDate = top.var_checkout.get()
    
    try:
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        no_of_days = abs((outDate - inDate).days)
        top.var_noofdays.set(no_of_days)
    except ValueError:
        messagebox.showerror("Error", "Invalid date format")
    
    room_type = e4.get()
    meal = e6.get()
    
    if meal == "BreakFast" and room_type == "Laxary":
        q1 = float(300)
        q2 = float(700)
        q3 = float(top.var_noofdays.get())
        q4 = float(q1 + q2)
        q5 = float(q3 + q4)
        tax = "Rs." + str("%.2f" % ((q5) * 0.1))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
        top.var_paidtax.set(tax)
        top.var_subtotal.set(ST)
        top.var_total.set(TT)

    

    elif meal == "Lunch" and room_type == "Laxary":
         q1 = float(800)
         q2 = float(1300)
         q3 = float(top.var_noofdays.get())
         q4 = float(q1 + q2)
         q5 = float(q3 + q4)
         tax = "Rs." + str("%.2f" % ((q5) * 0.1))
         ST = "Rs." + str("%.2f" % ((q5)))
         TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
         top.var_paidtax.set(tax)
         top.var_subtotal.set(ST)
         top.var_total.set(TT)


    elif meal == "Dinner" and room_type == "Laxary":
        q1 = float(800)
        q2 = float(1300)
        q3 = float(top.var_noofdays.get())
        q4 = float(q1 + q2)
        q5 = float(q3 + q4)
        tax = "Rs." + str("%.2f" % ((q5) * 0.1))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
        top.var_paidtax.set(tax)
        top.var_subtotal.set(ST)
        top.var_total.set(TT)

    elif meal == "BreakFast" and room_type == "Double":
        q1 = float(250)
        q2 = float(650)
        q3 = float(top.var_noofdays.get())
        q4 = float(q1 + q2)
        q5 = float(q3 + q4)
        tax = "Rs." + str("%.2f" % ((q5) * 0.1))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
        top.var_paidtax.set(tax)
        top.var_subtotal.set(ST)
        top.var_total.set(TT)

    

    elif meal == "Lunch" and room_type == "Double":
        q1 = float(500)
        q2 = float(1200)
        q3 = float(top.var_noofdays.get())
        q4 = float(q1 + q2)
        q5 = float(q3 + q4)
        tax = "Rs." + str("%.2f" % ((q5) * 0.1))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
        top.var_paidtax.set(tax)
        top.var_subtotal.set(ST)
        top.var_total.set(TT)


    elif meal == "Dinner" and room_type == "Double":
        q1 = float(500)
        q2 = float(1200)
        q3 = float(top.var_noofdays.get())
        q4 = float(q1 + q2)
        q5 = float(q3 + q4)
        tax = "Rs." + str("%.2f" % ((q5) * 0.1))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
        top.var_paidtax.set(tax)
        top.var_subtotal.set(ST)
        top.var_total.set(TT)

    elif meal == "BreakFast" and room_type == "Single":
        q1 = float(200)
        q2 = float(400)
        q3 = float(top.var_noofdays.get())
        q4 = float(q1 + q2)
        q5 = float(q3 + q4)
        tax = "Rs." + str("%.2f" % ((q5) * 0.1))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
        top.var_paidtax.set(tax)
        top.var_subtotal.set(ST)
        top.var_total.set(TT)

    elif meal == "Lunch" and room_type == "Single":
        q1 = float(400)
        q2 = float(700)
        q3 = float(top.var_noofdays.get())
        q4 = float(q1 + q2)
        q5 = float(q3 + q4)
        tax = "Rs." + str("%.2f" % ((q5) * 0.1))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
        top.var_paidtax.set(tax)
        top.var_subtotal.set(ST)
        top.var_total.set(TT)

    elif meal == "Dinner" and room_type == "Single":
        q1 = float(500)
        q2 = float(800)
        q3 = float(top.var_noofdays.get())
        q4 = float(q1 + q2)
        q5 = float(q3 + q4)
        tax = "Rs." + str("%.2f" % ((q5) * 0.1))
        ST = "Rs." + str("%.2f" % ((q5)))
        TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
        top.var_paidtax.set(tax)
        top.var_subtotal.set(ST)
        top.var_total.set(TT)



# top.var_check_in = StringVar()
# top.var_check_out = StringVar()
# top.var_no_of_days = StringVar()


#........................................................................................
l = Label(top, text="ROOMBOOKING DETAIL", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=3,relief=RIDGE)
l.place(x=0, y=0, width=1130, height=50)


path = r"C:\Users\Admin\OneDrive\Desktop\Images\images6.jpg"
img1 = Image.open(path)
img1.thumbnail((50, 45))  # Create thumbnail
img1 = ImageTk.PhotoImage(img1)

l2 = Label(top, image=img1,relief=RIDGE)
l2.place(x=2, y=0)  # Left side par image

l1 = LabelFrame(top,bd=2,relief=RIDGE,text="Roombooking details",font=("Arial 12 bold"),padx=2)
l1.place(x=5,y=50,width=375,height=490)

l2 = Label(l1,text="Contact",font=("Arial 12 bold"),padx=2,pady=6)
l2.grid(row=0,column=0,sticky=W)

e1 = ttk.Entry(l1,width=13,textvariable=top.var_contact,font=("Arial 13 bold"))
e1.grid(row=0,column=1,sticky=W)


l3 = Label(l1,text="Check_in",font=("Arial 12 bold"),padx=2,pady=6)
l3.grid(row=1,column=0,sticky=W)

e2 = ttk.Entry(l1,width=23,textvariable=top.var_checkin,font=("Arial 13 bold"))
e2.grid(row=1,column=1,sticky=W)

l4 = Label(l1,text="Check_out",font=("Arial 12 bold"),padx=2,pady=6)
l4.grid(row=2,column=0,sticky=W)

e3 = ttk.Entry(l1,width=23,textvariable=top.var_checkout,font=("Arial 13 bold"))
e3.grid(row=2,column=1,sticky=W)

l5 = Label(l1,text="Room Type",font=("Arial 12 bold"),padx=2,pady=6)
l5.grid(row=3,column=0,sticky=W)
db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
cur = db.cursor()
cur.execute("select room_type from detail")
#ide=cur.fetchall()

e4 = ttk.Combobox(l1,font=("Arial 12 bold"),textvariable=top.var_roomtype,width=21,state="readonly")
e4['values']=("Single","Double","Laxary")
e4.current(0)
e4.grid(row=3,column=1,sticky=W)

l6 = Label(l1,text="Available Room",font=("Arial 12 bold"),padx=2,pady=6)
l6.grid(row=4,column=0,sticky=W)
top.available_room = StringVar()
e5 = ttk.Combobox(l1,font=("Arial 12 bold"),textvariable=top.available_room,width=21,state="readonly")


db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
cur = db.cursor()
cur.execute("select room_no from detail")
rows=cur.fetchall()
e5 = ttk.Combobox(l1,font=("Arial 12 bold"),textvariable=top.available_room,width=21,state="readonly")
e5['values']=rows
e5.current(0)
e5.grid(row=4,column=1,sticky=W)

# e5 = ttk.Entry(l1,width=23,textvariable=top.var_available_room, font=("Arial 13 bold"))
# e5.grid(row=4,column=1,sticky=W)

l7 = Label(l1,text="Meal",font=("Arial 12 bold"),padx=2,pady=6)
l7.grid(row=5,column=0,sticky=W)


e6 = ttk.Combobox(l1, font=("Arial 12 bold"), textvariable=top.var_meal, width=21, state="readonly")
e6['values'] = ("BreakFast", "Lunch", "Dinner")
e6.current(0)
e6.grid(row=5, column=1, sticky=W)






l8 = Label(l1,text="No of Days",font=("Arial 12 bold"),padx=2,pady=6)
l8.grid(row=6,column=0,sticky=W)

e7 = ttk.Entry(l1,width=23,textvariable=top.var_noofdays,font=("Arial 13 bold"))
e7.grid(row=6,column=1,sticky=W)

l9 = Label(l1,text="Paid Tax",font=("Arial 12 bold"),padx=2,pady=6)
l9.grid(row=7,column=0,sticky=W)

e8 = ttk.Entry(l1,width=23,textvariable=top.var_paidtax,font=("Arial 13 bold"))
e8.grid(row=7,column=1,sticky=W)

l10 = Label(l1,text="Sub Total",font=("Arial 12 bold"),padx=2,pady=6)
l10.grid(row=8,column=0,sticky=W)

e9 = ttk.Entry(l1,width=23,textvariable=top.var_subtotal,font=("Arial 13 bold"))
e9.grid(row=8,column=1,sticky=W)

l11 = Label(l1,text="Total Cost",font=("Arial 12 bold"),padx=2,pady=6)
l11.grid(row=9,column=0,sticky=W)

e10 = ttk.Entry(l1,width=23,textvariable=top.var_total,font=("Arial 13 bold"))
e10.grid(row=9,column=1,sticky=W)

b2 = Button(l1,text="Bill",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=total)
b2.grid(row=10,column=0,sticky=W)

f1 = Frame(l1,bd=2,relief=RIDGE)
f1.place(x=0,y=400,width=365,height=40)

b3 = Button(f1,text="Add",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=add)
b3.grid(row=0,column=0)

b4 = Button(f1,text="Update",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=update)
b4.grid(row=0,column=1)

b5 = Button(f1,text="Delete",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=delete)
b5.grid(row=0,column=2)

b6 = Button(f1,text="Reset",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=reset)
b6.grid(row=0,column=3)

#............... Frame .............................................

f2 = LabelFrame(top,bd=2,relief=RIDGE,font=("Arial 12 bold"),padx=2)
f2.place(x=390,y=50,width=740,height=245)

#...........................Images................................................

path = r"C:\Users\Admin\OneDrive\Desktop\Images\premium_photo-1661877303180-19a028c21048.jpeg"
img3 = Image.open(path)
img3 = img3.resize((450, 250)) # Resize image
img3 = ImageTk.PhotoImage(img3)
l = Label(f2, image=img3)
l.image = img3  # Keep a reference to the image
l.place(x=0, y=0, width=1020, height=245)  # Adjust label size

#......................Frame ..........................................................

f4 = LabelFrame(top,bd=2,relief=RIDGE,font=("Arial 12 bold"),padx=2)
f4.place(x=390,y=50,width=290,height=245)



f3 = LabelFrame(top,bd=2,relief=RIDGE,text="View Details and Search System",font=("Arial 12 bold"),padx=2)
f3.place(x=390,y=305,width=740,height=235)

e12 = ttk.Combobox(f3,font=("Arial 12 bold"),width=23,state="readonly")
e12['values']=("Contact","Available_Room")
e12.current(0)
e12.grid(row=0,column=1,padx=2)

e13 = ttk.Entry(f3,width=23,font=("Arial 13 bold"))
e13.grid(row=0,column=2,padx=2)

b5 = Button(f3,text="Search",font=("Arial 13 bold"),bg='black',fg='gold',width=10,command=search)
b5.grid(row=0,column=3,padx=1)

b6 = Button(f3,text="Show",font=("Arial 13 bold"),bg='black',fg='gold',width=10,command=show)
b6.grid(row=0,column=4,padx=1)

#............show data.....................................................

f5 = Frame(f3,bd=2,relief=RIDGE)
f5.place(x=0,y=50,width=720,height=160)

scroll_x = ttk.Scrollbar(f5,orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(f5,orient=VERTICAL)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)



tv = ttk.Treeview(f5,selectmode="browse",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=tv.xview)
scroll_y.config(command=tv.yview)
tv['columns']=( 'Contact','Check_in','Check_out','Room_Type','Available_Room','Meal','No_of_Days','Paid_Tax','Sub_Total','Total_Cost')


tv.column('#0', width=0, stretch=NO)
for col in tv['columns']:
    tv.column(col,anchor=CENTER,width=100)
    for col in tv['column']:
        tv.heading(col,text=col,anchor=CENTER)
tv.column('Contact', anchor=CENTER, width=110)
tv.column('Check_in', anchor=CENTER, width=100)
tv.column('Check_out', anchor=CENTER, width=100)
tv.column('Room_Type', anchor=CENTER, width=100)
tv.column('Available_Room', anchor=CENTER, width=100)
tv.column('Meal', anchor=CENTER, width=100)
tv.column('No_of_Days', anchor=CENTER, width=100)
tv.column('Paid_Tax', anchor=CENTER, width=100)
tv.column('Sub_Total', anchor=CENTER, width=100)
tv.column('Total_Cost', anchor=CENTER, width=100)

tv["show"]="headings"

tv.heading('Contact', text='Contact', anchor=CENTER)
tv.heading('Check_in', text='Check_in', anchor=CENTER)
tv.heading('Check_out', text='Check_out', anchor=CENTER)
tv.heading('Room_Type', text='Room_Type', anchor=CENTER)
tv.heading('Available_Room', text='Available_Room', anchor=CENTER)
tv.heading('Meal', text='Meal', anchor=CENTER)
tv.heading('No_of_Days', text='No_of_Days', anchor=CENTER)
tv.heading('Paid_Tax', text='Paid_Tax', anchor=CENTER)
tv.heading('Sub_Total', text='Sub_Total', anchor=CENTER)
tv.heading('Total_Cost', text='Total_Cost', anchor=CENTER)

tv.pack(fill=BOTH,expand=1)
tv.fetch_data = fetch_data  # Method ko define karein
tv.fetch_data()  # Method ko call karein
tv.bind("<ButtonRelease-1>", lambda event: get_cursor(tv, event))


#............................fatch name...........................
def Fetch_contact():
    if top.var_contact.get()=="":
        messagebox.showerror("error","Please enter contact number",parent=top)
    else:
        db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
        cur = db.cursor()
        query=("select customer_name from customers where contact=%s")
        value=(top.var_contact.get(),)
        cur.execute(query,value)  # Corrected here
        row=cur.fetchone()

        if row==None:
            messagebox.showerror("Error","this number not found",parent=top)
        else:
            db.commit()
            db.close()




            lb1name=Label(f4,text="Name:",font=("Arial 13 bold"))
            lb1name.place(x=0,y=0)

            lb1=Label(f4,text=row,font=("Arial 13 bold"))
            lb1.place(x=90,y=0)
            
            

           


        #............gender.................................

        db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
        cur = db.cursor()
        query=("select gender from customers where contact=%s")
        value=(top.var_contact.get(),)
        cur.execute(query,value)  # Corrected here
        row=cur.fetchone()

        lb1gender=Label(f4,text="Gender:",font=("Arial 13 bold"))
        lb1gender.place(x=0,y=30)

        lb2=Label(f4,text=row,font=("Arial 13 bold"))
        lb2.place(x=90,y=30)

        
        #.....................email.........................

        db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
        cur = db.cursor()
        query=("select email from customers where contact=%s")
        value=(top.var_contact.get(),)
        cur.execute(query,value)  # Corrected here
        row=cur.fetchone()

        lb1email=Label(f4,text="Email:",font=("Arial 13 bold"))
        lb1email.place(x=0,y=60)

        lb3=Label(f4,text=row,font=("Arial 13 bold"))
        lb3.place(x=90,y=60)

        
        #......................nationality.......................

        db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
        cur = db.cursor()
        query=("select nationality from customers where contact=%s")
        value=(top.var_contact.get(),)
        cur.execute(query,value)  # Corrected here
        row=cur.fetchone()



        lb1nationality=Label(f4,text="Nationality:",font=("Arial 13 bold"))
        lb1nationality.place(x=0,y=90)

        lb4=Label(f4,text=row,font=("Arial 13 bold"))
        lb4.place(x=90,y=90)

        #.........................Address............................

        db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
        cur = db.cursor()
        #query=("select address from customers where contact=%s")
        query=("select address from customers where contact=%s")
        value=(top.var_contact.get(),)
        cur.execute(query,value)  # Corrected here
        row=cur.fetchone()

        lb1address=Label(f4,text="address:",font=("Arial 13 bold"))
        lb1address.place(x=0,y=120)

        lb4=Label(f4,text=row,font=("Arial 13 bold"))
        lb4.place(x=90,y=120)




        

#...................fetch button.............................................
b1 = Button(l1,text="Fetch Data",font=("Arial 8 bold"),bg='black',fg='gold',width=8,command=Fetch_contact)
b1.place(x=280,y=4)



top.mainloop()