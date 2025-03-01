from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.geometry('1139x550+230+150')
root.title("hotel management")


import pymysql as sql
db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
cur = db.cursor()

def customer_page(root):
    root.var_customer_ref = StringVar()
    f3 = Frame(root, height=500, width=1500, bg='white', relief=RIDGE)
    f3.place(x=0, y=191)
#......................variables...........................................
root.var_customer_ref = StringVar()
root.var_customer_name = StringVar()
root.var_mother_name = StringVar()
root.var_gender = StringVar()
root.var_post_code = StringVar()
root.var_contact = StringVar()
root.var_email = StringVar()
root.var_nationality = StringVar()
root.var_id_proof = StringVar()
root.var_id_number = StringVar()
root.var_address = StringVar()


#...........................Add.........................................................
def add_customer():
    customer_ref = e1.get()
    customer_name = e2.get()
    mother_name = e3.get()
    gender = e4.get()
    post_code = e5.get()
    contact = e6.get()
    email = e7.get()
    nationality = e8.get()
    id_proof_type = e9.get()
    id_number = e10.get()
    address = e11_address.get()
    if not all([customer_ref,customer_name,mother_name,gender,post_code,contact,email,nationality,id_proof_type,id_number,address]):
        messagebox.showerror("Error","please fill all fields")
        return
    try:
        cur.execute("INSERT INTO customers (customer_ref, customer_name, mother_name, gender, post_code, contact, email, nationality, id_proof_type, id_number, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (customer_ref, customer_name, mother_name, gender, post_code, contact, email, nationality, id_proof_type, id_number, address))
        db.commit()
        if cur.rowcount > 0:
            messagebox.showinfo("Success", "Record inserted successfully")
            e1.delete(0,"end")
            e2.delete(0,"end")
            e3.delete(0,"end")
            e4.set("")
            e5.delete(0,"end")
            e6.delete(0,"end")
            e7.delete(0,"end")
            e8.set("")
            e9.set("")
            e10.delete(0,"end")
            e11_address.delete(0,"end")
        else:
            messagebox.showerror("Error", "Record not inserted")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        db.commit()

#....................................update..........................................................
def update():
    k1 = e1.get()
    k2 = e2.get()
    k3 = e3.get()
    k4 = e4.get()
    k5 = e5.get()
    k6 = e6.get()
    k7 = e7.get()
    k8 = e8.get()
    k9 = e9.get()
    k10 = e10.get()
    k11 = e11_address.get()
    cur.execute("update customers set customer_name=%s, mother_name=%s, gender=%s, post_code=%s, contact=%s, email=%s, nationality=%s, id_proof_type=%s, id_number=%s, address=%s where customer_ref=%s", (k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k1))
    db.commit()
    if cur.rowcount > 0:
        messagebox.showinfo('result', 'record updated successfully')
        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.set("")
        e5.delete(0, "end")
        e6.delete(0, "end")
        e7.delete(0, "end")
        e8.set("")
        e9.set("")
        e10.delete(0, "end")
        e11_address.delete(0, "end")
    else:
        messagebox.showinfo('result', 'record not updated')

#....................................delete..................................................
def delete():
    k = e1.get()
    cur.execute("delete from customers where customer_ref=%s", (k,))
    db.commit()
    if cur.rowcount > 0:
        messagebox.showinfo('result', 'record deleted successfully')
        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.set("")
        e5.delete(0, "end")
        e6.delete(0, "end")
        e7.delete(0, "end")
        e8.set("")
        e9.set("")
        e10.delete(0, "end")
        e11_address.delete(0, "end")
    else:
        messagebox.showinfo('result', 'record not deleted')

#............................reset...........................................................
def reset():
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.set("")
    e5.delete(0, "end")
    e6.delete(0, "end")
    e7.delete(0, "end")
    e8.set("")
    e9.set("")
    e10.delete(0, "end")
    e11_address.delete(0, "end")

#...............................search.........................................................
def search():
    for i in tv.get_children():
        tv.delete(i)
    query = e13.get()
    query_type = e12.get()
    if query_type == "contact":
        cur.execute("select * from customers where contact=%s", (query,))
    elif query_type == "Ref":
        cur.execute("select * from customers where customer_ref=%s", (query,))
    result = cur.fetchall()
    if len(result) > 0:
        for col in result:
            tv.insert("", 'end', values=col)
    else:
        messagebox.showinfo("result", "record not found")



#.......................................show...............................................................
def show():
    for i in tv.get_children():
        tv.delete(i)
    cur.execute("select * from customers")
    result = cur.fetchall()
    if len(result) > 0:
        for col in result:
            tv.insert("", 'end', values=col)
    else:
        messagebox.showinfo("result", "record not found")

#........................fetch data.................................
def fetch_data():
    tv.delete(*tv.get_children())
    db=sql.connect(host='localhost',user='root',password='rishu123',db='project3')
    cur = db.cursor()
    cur.execute("select * from customers")
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
            root.var_customer_ref.set(row[0])
            root.var_customer_name.set(row[1])
            root.var_mother_name.set(row[2])
            root.var_gender.set(row[3])
            root.var_post_code.set(row[4])
            root.var_contact.set(row[5])
            root.var_email.set(row[6])
            root.var_nationality.set(row[7])
            root.var_id_proof.set(row[8])
            root.var_id_number.set(row[9])
            root.var_address.set(row[10])
        except Exception as e:
            messagebox.showerror("Error", str(e))








l = Label(root, text="ADD CUSTOMER DETAIL", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=3,relief=RIDGE)
l.place(x=0, y=0, width=1130, height=50)

#path = r"C:\Users\Admin\Desktop\Images\images6.jpg"
path = r"C:\Users\Admin\OneDrive\Desktop\Images\images6.jpg"
img1 = Image.open(path)
img1.thumbnail((50, 45))  # Create thumbnail
img1 = ImageTk.PhotoImage(img1)

l2 = Label(root, image=img1,relief=RIDGE)
l2.place(x=2, y=0)  # Left side par image

l1 = LabelFrame(root,bd=2,relief=RIDGE,text="customer details",font=("Arial 12 bold"),padx=2)
l1.place(x=5,y=50,width=375,height=490)

l2 = Label(l1,text="customer ref",font=("Arial 12 bold"),padx=2,pady=6)
l2.grid(row=0,column=0,sticky=W)


e1 = ttk.Entry(l1,width=26,textvariable=root.var_customer_ref,font=("Arial 13 bold"))
e1.grid(row=0,column=1,sticky=W)




l3 = Label(l1,text="customer name",font=("Arial 12 bold"),padx=2,pady=6)
l3.grid(row=1,column=0,sticky=W)

e2 = ttk.Entry(l1,width=26,textvariable=root.var_customer_name,font=("Arial 13 bold"))
e2.grid(row=1,column=1,sticky=W)

l4 = Label(l1,text="Mother Name",font=("Arial 12 bold"),padx=2,pady=6)
l4.grid(row=2,column=0,sticky=W)

e3 = ttk.Entry(l1,width=26,textvariable=root.var_mother_name,font=("Arial 13 bold"))
e3.grid(row=2,column=1,sticky=W)

l5 = Label(l1,text="Gender",font=("Arial 12 bold"),padx=2,pady=6)
l5.grid(row=3,column=0,sticky=W)

e4 = ttk.Combobox(l1,font=("Arial 12 bold"),textvariable=root.var_gender,width=23,state="readonly")
e4['values']=("Male","Female","Other")
e4.current(0)
e4.grid(row=3,column=1,sticky=W)


l6 = Label(l1,text="PostCode",font=("Arial 12 bold"),padx=2,pady=6)
l6.grid(row=4,column=0,sticky=W)

e5 = ttk.Entry(l1,width=26,textvariable=root.var_post_code,font=("Arial 13 bold"))
e5.grid(row=4,column=1,sticky=W)


l7 = Label(l1,text="contact",font=("Arial 12 bold"),padx=2,pady=6)
l7.grid(row=5,column=0,sticky=W)

e6 = ttk.Entry(l1,width=26,textvariable=root.var_contact,font=("Arial 13 bold"))
e6.grid(row=5,column=1,sticky=W)


l8 = Label(l1,text="Email",font=("Arial 12 bold"),padx=2,pady=6)
l8.grid(row=6,column=0,sticky=W)

e7 = ttk.Entry(l1,width=26,textvariable=root.var_email,font=("Arial 13 bold"))
e7.grid(row=6,column=1,sticky=W)


l9 = Label(l1,text="Nationality:",font=("Arial 12 bold"),padx=2,pady=6)
l9.grid(row=7,column=0,sticky=W)

e8 = ttk.Combobox(l1,font=("Arial 12 bold"),textvariable=root.var_nationality,width=23,state="readonly")
e8['values']=("Indian","American","British")
e8.current(0)
e8.grid(row=7,column=1,sticky=W)



l10 = Label(l1,text="Id Proof Type:",font=("Arial 12 bold"),padx=2,pady=6)
l10.grid(row=8,column=0,sticky=W)


e9 = ttk.Combobox(l1,font=("Arial 12 bold"),textvariable=root.var_id_proof,width=23,state="readonly")
e9['values']=("Aadhar card","passport","pencard")
e9.current(0)
e9.grid(row=8,column=1,sticky=W)




l11 = Label(l1,text="Id Number:",font=("Arial 12 bold"),padx=2,pady=6)
l11.grid(row=9,column=0,sticky=W)

e10 = ttk.Entry(l1,width=26,textvariable=root.var_id_number,font=("Arial 13 bold"))
e10.grid(row=9,column=1,sticky=W)


l12 = Label(l1,text="Address:",font=("Arial 12 bold"),padx=2,pady=6)
l12.grid(row=10,column=0,sticky=W)

e11_address = ttk.Entry(l1,width=26,textvariable=root.var_address,font=("Arial 13 bold"))
e11_address.grid(row=10,column=1,sticky=W)

f1 = Frame(l1,bd=2,relief=RIDGE)
f1.place(x=0,y=400,width=365,height=40)

b1 = Button(f1,text="Add",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=add_customer)
b1.grid(row=0,column=0)

b2 = Button(f1,text="Update",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=update)
b2.grid(row=0,column=1)

b3 = Button(f1,text="Delete",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=delete)
b3.grid(row=0,column=2)

b4 = Button(f1,text="Reset",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=reset)
b4.grid(row=0,column=3)

f2 = LabelFrame(root,bd=2,relief=RIDGE,text="view details and search system",font=("Arial 12 bold"),padx=2)
f2.place(x=390,y=50,width=735,height=490)

l13 = Label(f2,text="Search",font=("Arial 12 bold"),bg='red',fg='white')
l13.grid(row=0,column=0)

e12 = ttk.Combobox(f2,font=("Arial 12 bold"),width=23,state="readonly")
e12['values']=("contact","Ref")
e12.current(0)
e12.grid(row=0,column=1)

e13 = ttk.Entry(f2,width=23,font=("Arial 13 bold"))
e13.grid(row=0,column=2)

b5 = Button(f2,text="Search",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=search)
b5.grid(row=0,column=3)

b6 = Button(f2,text="Show",font=("Arial 13 bold"),bg='black',fg='gold',width=8,command=show)
b6.grid(row=0,column=4)



f3 = Frame(f2,bd=2,relief=RIDGE)
f3.place(x=0,y=50,width=700,height=390)

scroll_x = ttk.Scrollbar(f3,orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(f3,orient=VERTICAL)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)



tv = ttk.Treeview(f3,selectmode="browse",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=tv.xview)
scroll_y.config(command=tv.yview)
tv['columns']=( 'customer_ref','customer_name','mother_name','gender','post_code','contact','email','nationality','id_proof_type','id_number','address')

tv.column('#0', width=0, stretch=NO)
for col in tv['columns']:
    tv.column(col,anchor=CENTER,width=100)
    for col in tv['column']:
        tv.heading(col,text=col,anchor=CENTER)
#tv.column('customer_id', anchor=CENTER, width=100)
tv.column('customer_ref', anchor=CENTER, width=100)
tv.column('customer_name', anchor=CENTER, width=100)
tv.column('mother_name', anchor=CENTER, width=100)
tv.column('gender', anchor=CENTER, width=100)
tv.column('post_code', anchor=CENTER, width=100)
tv.column('contact', anchor=CENTER, width=100)
tv.column('email', anchor=CENTER, width=100)
tv.column('nationality', anchor=CENTER, width=100)
tv.column('id_proof_type', anchor=CENTER, width=100)
tv.column('id_number', anchor=CENTER, width=100)
tv.column('address', anchor=CENTER, width=100)

tv["show"]="headings"

#tv.heading('customer_id', text='customer_id', anchor=CENTER)
tv.heading('customer_ref', text='customer_ref', anchor=CENTER)
tv.heading('customer_name', text='customer_name', anchor=CENTER)
tv.heading('mother_name', text='mother_name', anchor=CENTER)
tv.heading('gender', text='gender', anchor=CENTER)
tv.heading('post_code', text='post_code', anchor=CENTER)
tv.heading('contact', text='contact', anchor=CENTER)
tv.heading('email', text='email', anchor=CENTER)
tv.heading('nationality', text='nationality', anchor=CENTER)
tv.heading('id_proof_type', text='id_proof_type', anchor=CENTER)
tv.heading('id_number', text='id_number', anchor=CENTER)
tv.heading('address', text='address', anchor=CENTER)

tv.pack(fill=BOTH,expand=1)
tv.fetch_data = fetch_data  # Method ko define karein
tv.fetch_data()  # Method ko call karein
tv.bind("<ButtonRelease-1>", lambda event: get_cursor(tv, event))





root.mainloop()