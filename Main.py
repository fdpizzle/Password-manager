import tkinter
from tkinter import messagebox
from random import randint
window = tkinter.Tk()
window.title("Login")
window.geometry('340x440')
window.configure(bg='#333333')
def open_password_manager():
    pm = tkinter.Toplevel(window)
    pm.title("Password Manager")
    pm.geometry("500x300")
    def new_rand():
        pw_entry.delete(0, tkinter.END)
        try:
            pw_length = int(my_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter a number for password length.")
            return

        my_password = ""
        for x in range(pw_length):
            my_password += chr(randint(33,126))

        pw_entry.insert(0, my_password)

    def clipper():
        pm.clipboard_clear()
        pm.clipboard_append(pw_entry.get())

    lf = tkinter.LabelFrame(pm, text="Input how many characters you would like your password to be")
    lf.pack(pady=20)

    my_entry = tkinter.Entry(lf, font=("Helvetica", 24))
    my_entry.pack(pady=20, padx=20)

    pw_entry = tkinter.Entry(pm, text="", font=("Helvetica,", 25), bd=0, bg="systembuttonface")
    pw_entry.pack(pady=20)

    frame = tkinter.Frame(pm)
    frame.pack(pady=20)

    my_button = tkinter.Button(frame, text="Click here to generate strong password", command=new_rand)
    my_button.grid(row=0, column=0, padx=10)

    clip_button = tkinter.Button(frame, text="Click here to copy password to clipboard", command=clipper)
    clip_button.grid(row=0, column=1, padx=10)
    def logout():
        pm.destroy()
        window.deiconify()  

    logout_btn = tkinter.Button(pm, text="Logout", command=logout)
    logout_btn.pack(pady=5)


def login():
    username = "Franky"
    password = "12345"

    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login", message="Login Success!")
        window.withdraw()           
        open_password_manager()     
    else:
        messagebox.showerror(title="Login", message="Login was unsuccessful. Please try again")
frame = tkinter.Frame(bg='#333333')
login_label = tkinter.Label(frame, text="Login", bg='#333333', fg="#FFFFFF", font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, bg='#333333', fg="#FFFFFF", font=("Arial", 16), insertbackground="white")
password_entry = tkinter.Entry(frame, show="*", bg='#333333', fg="#FFFFFF", font=("Arial", 16), insertbackground="white")
password_label = tkinter.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg='#333333', fg="#FFFFFF", font=("Arial", 16), command=login)
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
frame.pack()
password_entry.bind("<Return>", lambda e: login())

window.mainloop()
