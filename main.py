import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as messagebox
import sqlite3 

win =tk.Tk()
win.geometry("1550x1000")
win.title("Blood Bank Management System")
win.resizable(0,0)


conn = sqlite3.connect("user.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS employee (
    donorname TEXT,
    gender TEXT,
    address TEXT,
    phone INT,
    dob INT,
    age INT,
    bloods TEXT,
    unit INT
)
""")

conn.commit()
conn.close()


def add():
    if len(phone.get()) != 10:
        messagebox.showerror("Error!", "Please enter all the fields correctly.", parent=win)
    else:
        conn = sqlite3.connect("user.db")
        c = conn.cursor()

        c.execute("""
        INSERT INTO employee(donorname, gender, address, phone, dob, age, bloods, unit) 
        VALUES(?,?,?,?,?,?,?,?)
        """, (
            donorname.get(),
            gender_var.get(),
            address.get(),
            phone.get(),
            dob.get(),
            age.get(),
            bloods.get(),
            unit.get()
        ))

        conn.commit()
        conn.close()

        display_data()



def update():
    selected_item = donor_table.selection()

    if selected_item:
        # Get the donor ID from the selected item in the treeview
        selected_donor_id = donor_table.item(selected_item, "values")[6]  # Assuming the Donor ID is at index 6

        conn = sqlite3.connect("user.db")
        c = conn.cursor()

        c.execute("""
        UPDATE employee 
        SET donorname=?, gender=?, address=?, phone=?, dob=?, age=?, bloods=?, unit=? 
        WHERE id=?
        """, (   
            donorname.get(),
            gender_var.get(),
            address.get(),
            phone.get(),
            dob.get(),
            age.get(),
            bloods.get(),
            unit.get(),
            selected_donor_id
        ))
        conn.commit()
        conn.close()

        display_data()
    else:
        print("Please select a donor from the table for updating")

        

def delete():
    # Get the selected item in the treeview
    selected_item = donor_table.selection()

    if selected_item:
        # Get the values of the selected item
        values = donor_table.item(selected_item, 'values')

        # Assuming Donor ID is the first column
        selected_donor_id = values[6]  # Update the index based on your data

        # Check if Donor ID is provided
        if selected_donor_id:
            conn = sqlite3.connect("blood.db")
            c = conn.cursor()

            c.execute("DELETE FROM employee WHERE id=?", (selected_donor_id,))

            conn.commit()
            conn.close()

            # Display updated data
            display_data()
        else:
            print("Donor ID not found for deletion")
    else:
        print("No item selected for deletion")


def reset():
    donorname.set("")
    gender_var.set("")
    address.set("")
    phone.set("")
    dob.set("")
    age.set("")
    id.set("")
    bloods.set("")
    unit.set("")


def display_data():
    # Clear existing data in the treeview
    for record in donor_table.get_children():
        donor_table.delete(record)

    conn = sqlite3.connect("user.db")
    c = conn.cursor()

    search_column = search_in.get()
    search_value = search_entry.get()

    # If search criteria is provided, fetch data accordingly
    if search_column and search_value:
        # Modify the query to use the correct column name
        query = f"SELECT * FROM employee WHERE `{search_column.lower()}` LIKE ?"
        c.execute(query, (f"%{search_value}%",))
    else:
        c.execute("SELECT * FROM employee")

    data = c.fetchall()

    if not data:
        messagebox.showerror("Not Available", "No records found.")
    else:
        for record in data:
            donor_table.insert("", "end", values=record)

    conn.close()

def search():
    display_data()


# Global variable for treeview
donor_table = None


title_label= tk.Label(win, text="Blood Bank Management System",font=("Ariel",30,"bold"),foreground="black",border=12,relief=tk.GROOVE,bg="red")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame=tk.LabelFrame(win,text="Donor Details",font=("Ariel",20,"bold","italic"),bd=12,relief=tk.GROOVE,bg="lightgrey")
detail_frame.place(x=30,y=90,width=470,height=700)

data_frame=tk.Frame(win,bd=12,bg="white",relief=tk.GROOVE)
data_frame.place(x=520,y=90,width=1000,height=700)


#============ Variables ===========#

donorname = tk.StringVar()
gender_var=tk.StringVar()
address= tk.StringVar()
phone = tk.StringVar()
dob = tk.StringVar()
age = tk.StringVar()
id = tk.StringVar()
bloods = tk.StringVar()
unit = tk.StringVar()

search_by =tk.StringVar()

#============================#




#====== ENTRY ========#

donorname_lbl= tk.Label(detail_frame,text="Donor name", font=("Arial",17,"bold"),bg="lightgrey")
donorname_lbl.grid(row=1,column=0,padx=2,pady=2)

donorname_ent= tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=donorname)
donorname_ent.grid(row=1,column=1,padx=2,pady=2)

gender_frame = tk.Frame(detail_frame, bg="lightgrey")
gender_frame.grid(row=2, column=1, columnspan=2, padx=2, pady=2)

# Add a label "Gender" to the gender_frame
gender_lbl = tk.Label(detail_frame, text="Gender", font=("Arial", 17, "bold"), bg="lightgrey")
gender_lbl.grid(row=2, column=0, padx=2, pady=2)

gender_var = tk.StringVar()
gender_var.set("Male")  # Set the default value to Male

male_radio = tk.Radiobutton(gender_frame, text="Male", font=("Ariel", 15), variable=gender_var, value="Male", bg="lightgrey")
male_radio.grid(row=0, column=0, padx=2, pady=2)

female_radio = tk.Radiobutton(gender_frame, text="Female", font=("Ariel", 15), variable=gender_var, value="Female", bg="lightgrey")
female_radio.grid(row=0, column=1, padx=2, pady=2)


address_lbl= tk.Label(detail_frame,text="Address", font=("Ariel",17,"bold"),bg="lightgrey")
address_lbl.grid(row=3,column=0,padx=2,pady=2)

address_ent= tk.Entry(detail_frame,bd=7,font=("Ariel",15),textvariable=address)
address_ent.grid(row=3,column=1,padx=2,pady=2)

phone_lbl= tk.Label(detail_frame,text="Mobile Number", font=("Ariel",17,"bold"),bg="lightgrey")
phone_lbl.grid(row=4,column=0,padx=2,pady=2)

phone_ent= tk.Entry(detail_frame,bd=7,font=("Ariel",15),textvariable=phone)
phone_ent.grid(row=4,column=1,padx=2,pady=2)

dob_lbl= tk.Label(detail_frame,text="D.O.B", font=("Ariel",17,"bold"),bg="lightgrey")
dob_lbl.grid(row=5,column=0,padx=2,pady=2)

dob_ent= tk.Entry(detail_frame,bd=7,font=("Ariel",15),textvariable=dob)
dob_ent.grid(row=5,column=1,padx=2,pady=2)


age_lbl= tk.Label(detail_frame,text="Age",font=("Ariel",17,"bold"),bg="lightgrey")
age_lbl.grid(row=6,column=0,padx=2,pady=2)

age_ent= tk.Entry(detail_frame,bd=7,font=("Ariel",15),textvariable=age)
age_ent.grid(row=6,column=1,padx=2,pady=2)

# id_lbl= tk.Label(detail_frame,text="Donar ID",font=("Ariel",17,"bold"),bg="lightgrey")
# id_lbl.grid(row=7,column=0,padx=2,pady=2)

# id_ent= tk.Entry(detail_frame,bd=7,font=("Ariel",15),textvariable=id)
# id_ent.grid(row=7,column=1,padx=2,pady=2)

blood_lbl= tk.Label(detail_frame,text="Blood type",font=("Ariel",17,"bold"),bg="lightgrey")
blood_lbl.grid(row=8,column=0,padx=2,pady=2)

bloods_ent= tk.Entry(detail_frame,bd=7,font=("Ariel",15),textvariable=bloods)
bloods_ent.grid(row=8,column=1,padx=2,pady=2)


unit_lbl= tk.Label(detail_frame,text="Unit(in ml)",font=("Ariel",17,"bold"),bg="lightgrey")
unit_lbl.grid(row=9,column=0,padx=2,pady=2)

unit_ent= tk.Entry(detail_frame,bd=7,font=("Ariel",15),textvariable=unit)
unit_ent.grid(row=9,column=1,padx=2,pady=2)

#=========== entry end==========#

#=========== button ============#

btn_frame= tk.Frame(detail_frame, bg="black",bd=15,relief=tk.GROOVE)
btn_frame.place(x=20,y=500,width=400,height=120)

add_btn= tk.Button(btn_frame,bg="lightgrey",text="ADD",bd=7,font=("ariel",13,"bold","italic"),width=16, command=add)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn= tk.Button(btn_frame,bg="lightgrey",text="UPDATE",bd=7,font=("ariel",13,"bold","italic"),width=16, command=update)
update_btn.grid(row=0,column=1,padx=2,pady=2)

Delete_btn= tk.Button(btn_frame,bg="lightgrey",text="DELETE",bd=7,font=("ariel",13,"bold","italic"),width=16, command=delete)
Delete_btn.grid(row=1,column=0,padx=2,pady=2)

Reset_btn= tk.Button(btn_frame,bg="lightgrey",text="RESET",bd=7,font=("ariel",13,"bold","italic"),width=16, command=reset)
Reset_btn.grid(row=1,column=1,padx=2,pady=2)

#================   ============#


#=========== Search ========#



search_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text="SEARCH", bg="lightgrey", font=("Ariel", 14))
search_lbl.grid(row=0, column=0, padx=2, pady=2)

search_in = ttk.Combobox(search_frame, font=("ariel", 14), state="readonly")
search_in["values"] = ("Donorname", "Gender", "Address", "Phone", "DOB", "Age", "Bloods", "Unit")
search_in.grid(row=0, column=1, padx=12, pady=2)

search_entry = tk.Entry(search_frame, bd=7, font=("Ariel", 14))
search_entry.grid(row=0, column=2, padx=2, pady=2)

search_btn = tk.Button(search_frame, text="Search", font=("ariel", 13), bd=9, width=14, bg="lightgrey", command=search)
search_btn.grid(row=0, column=3, padx=12, pady=2)

showall_btn = tk.Button(search_frame, text="Show all", font=("Ariel", 13), bd=9, width=14, bg="lightgrey", command=display_data)
showall_btn.grid(row=0, column=4, padx=12, pady=2)


#================ ============#

#====== database frame========#

main_frame=tk.Frame(data_frame,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(data_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(data_frame,orient=tk.HORIZONTAL)

donor_table= ttk.Treeview(main_frame,columns=("Donor Name:","Gender:","Address:","Mobile Number:","D.O.B:","Age:","Donar ID:","Blood type:","Unit(in ml):"))

y_scroll.config(command=donor_table.yview)
x_scroll.config(command=donor_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

donor_table.heading("Donor Name:",text="Donor Name:")
donor_table.heading("Gender:",text="Gender:")
donor_table.heading("Address:",text="Address:")
donor_table.heading("Mobile Number:",text="Mobile Number:")
donor_table.heading("D.O.B:",text="D.O.B:")
donor_table.heading("Age:",text="Age:")
donor_table.heading("Donar ID:",text="Donor ID:")
donor_table.heading("Blood type:",text="Blood type:")
donor_table.heading("Unit(in ml):",text="Unit(in ml):")


donor_table["show"]= 'headings'

donor_table.column("Donor Name:",width=100)
donor_table.column("Gender:",width=100)
donor_table.column("Address:",width=100)
donor_table.column("Mobile Number:",width=100)
donor_table.column("D.O.B:",width=100)
donor_table.column("Age:",width=100)
donor_table.column("Donar ID:",width=100)
donor_table.column("Blood type:",width=100)
donor_table.column("Unit(in ml):",width=100)




donor_table.pack(fill=tk.BOTH,expand=True)




win.mainloop()