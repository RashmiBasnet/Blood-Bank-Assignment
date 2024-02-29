from tkinter import *
from tkinter import messagebox
import sqlite3

sign_up_window = None
login_window = None  # Add a variable to store the login window

def create_users_table():
    # Connect to the SQLite database
    conn = sqlite3.connect("user.db")
    c = conn.cursor()

    # Create the users table if it doesn't exist
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the users table
create_users_table()

def register_user():
    # Retrieve user inputs
    first_name = e3.get()
    last_name = e4.get()
    email = e5.get()
    password = e6.get()

    # Validate if required fields are not empty
    if not (first_name and last_name and email and password):
        messagebox.showerror("Error", "Please fill out all the fields")
        return

    # Connect to the SQLite database
    conn = sqlite3.connect("user.db")
    c = conn.cursor()

    # Check if the email already exists in the database
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    existing_user = c.fetchone()

    if existing_user:
        messagebox.showerror("Error", "User with this email already exists")
    else:

        # Insert the new user into the database
        c.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
                  (first_name, last_name, email, password))

        # Commit changes
        conn.commit()

        # Close the connection
        conn.close()

        # Destroy the registration window
        if sign_up_window and not sign_up_window.winfo_ismapped():
            sign_up_window.destroy()

        messagebox.showinfo("Success", "Registration successful!")

        open_login_window()


def open_login_window():
    global login_window
    import login as login
    if sign_up_window and not sign_up_window.winfo_ismapped():
        sign_up_window.destroy()

    # Open the login window
    login.create_login_window()
    
def create_registration_window():
    # Create a new Tkinter window for user registration
    global sign_up_window
    sign_up_window = Tk()
    sign_up_window.geometry("800x500")
    sign_up_window.title("Register")
    sign_up_window.config(bg="#F8F9F9")

    # Register labels and entry widgets
    reg = Label(sign_up_window, text="REGISTER", font=('Times New Roman', 23), background='#F8F9F9').place(x=530, y=80)
    fnam = Label(sign_up_window, text="First Name", bg="#F8F9F9").place(x=350, y=150)
    global e3
    e3 = Entry(sign_up_window, background="#F8F9F9")
    e3.place(x=430, y=150)

    lnam = Label(sign_up_window, text="Last Name", bg="#F8F9F9").place(x=350, y=180)
    global e4
    e4 = Entry(sign_up_window, background="#F8F9F9")
    e4.place(x=430, y=180)

    email_lbl = Label(sign_up_window, text="Email", bg="#F8F9F9").place(x=350, y=210)
    global e5
    e5 = Entry(sign_up_window, background="#F8F9F9")
    e5.place(x=430, y=210)

    password_lbl = Label(sign_up_window, text="Password", bg="#F8F9F9").place(x=350, y=240)
    global e6
    e6 = Entry(sign_up_window, show="**", background="#F8F9F9")
    e6.place(x=430, y=240)

    # Register button
    Button(sign_up_window, padx=5, pady=5, text="Register", bg="sky blue", command=register_user, fg="blue").place(x=550, y=290)

    # Back to login button
    Button(sign_up_window, padx=5, pady=5, text="Back to Login", bg="lightgrey", command=open_login_window).place(x=670, y=290)

    sign_up_window.mainloop()

if __name__ == "__main__":
    create_registration_window()