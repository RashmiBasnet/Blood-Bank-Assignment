from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as ttk
from PIL import ImageTk,Image

def open_main_window():
    blood.destroy()  # Destroy the login window
    import registration # Import and open the main window

def open_registration_window():
    blood.destroy()  # Destroy the login window
    import registration
    registration.create_registration_window()  # Call the function to create the registration window

blood = Tk()
blood.geometry("1000x500")
blood.title("Login")
blood.config(bg="#F8F9F9")
frame1=Frame(blood,width=430,height=350).place(x=40,y=60)
logo=Image.open("C:/Users/Aashra/OneDrive/Desktop/ragat.png").resize((500,400))
logo_tk=ImageTk.PhotoImage(logo)
my_label=ttk.Label(frame1,image=logo_tk)
my_label.place(x=5,y=0)

frame = Frame(blood, width=330, height=300).place(x=520, y=60)

# Email
def on_enter(e):
    name = e1.get()
    if name == "":
        e1.delete(0, "end")
    elif name == "abc@gmail.com":
        e1.delete(0, "end")
    else:
        e1.delete(0, "end")
        e1.insert(0, name)

def on_leave(e):
    name = e1.get()
    if name == "":
        e1.insert(0, "abc@gmail.com")
    else:
        pass

stid = Label(blood, text="Admin Email", background='#F8F9F9').place(x=600, y=150)
e1 = Entry(blood, background='#F8F9F9', fg="grey")
e1.place(x=690, y=150)
e1.insert(0, "abc@gmail.com")
e1.bind('<FocusIn>', on_enter)
e1.bind("<FocusOut>", on_leave)

def open_registration_window():
    global blood

    # Destroy the login window
    blood.destroy()

    import registration
    registration.create_registration_window()

# Password
def on_enter_password(e):
    name = e2.get()
    if name == "":
        e2.delete(0, "end")
    elif name == "password":
        e2.delete(0, "end")
    else:
        e2.delete(0, "end")
        e2.insert(0, name)

def on_leave_password(e):
    name = e2.get()
    if name == "":
        e2.insert(0, "password")

password = Label(blood, text="Password", background='#F8F9F9').place(x=600, y=190)
e2 = Entry(blood, show="**", background='#F8F9F9', fg="grey")
e2.place(x=690, y=190)
e2.insert(0, "password")
e2.bind('<FocusIn>', on_enter_password)
e2.bind("<FocusOut>", on_leave_password)

# Log Function
def login():
    user = e1.get()
    pw = e2.get()

    # Connect to the SQLite database
    conn = sqlite3.connect("user.db")
    c = conn.cursor()

    # # Hash the password
    # hashed_password = hashlib.sha256(pw.encode()).hexdigest()

    # Check if the email and hashed password match the database
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (user, pw))
    authenticated_user = c.fetchone()

    if authenticated_user:
        blood.destroy()  # Destroy the login window
        import registration  # Import and open the main window
    elif user == "" or pw == "":
        messagebox.showerror("Invalid", "Please fill out the fields")
    else:
        messagebox.showerror("Invalid", "Invalid Email and Password")

# LoginButton
Button(blood, padx=5, pady=5, text="Login", bg="sky blue", command=login, fg="blue").place(x=740, y=240)

# RegisterWay
def sign():
    open_registration_window()

Label(blood, text="Don't have an account?", bg="#F8F9F9", border=0).place(x=655, y=290)
sign_up = Button(blood, text="Sign Up", bg="#F8F9F9", fg="blue", command=sign).place(x=800, y=290)  # opens registration form window

blood.img =ImageTk
blood.mainloop()