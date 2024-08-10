from tkinter import *
from tkinter import messagebox
import os
from pwgenerator import pw_gen
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_rand_password():
    pwd_rand = pw_gen()
    pyperclip.copy(pwd_rand)
    pw_e.insert(END, pwd_rand)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    wb_e_hold = wb_e.get()
    un_e_hold = un_e.get()
    pw_e_hold = pw_e.get()
    # message box to assess whether the user is happy or not with the message
    if len(wb_e_hold) == 0 or len(pw_e_hold) == 0:
        messagebox.showerror(title="OOPS!", message="Please fill the entries")
    else:
        is_ok = messagebox.askokcancel(title=wb_e_hold, message="Are the data correct ?")
        if is_ok:
            # First check if the file exist !
            if os.path.isfile("./data.txt"):
                with open("data.txt", mode="a") as site:
                    site.write(wb_e_hold + " / " + un_e_hold + " / " + pw_e_hold + "\n")
            else:
                with open("data.txt", mode="w") as site:
                    site.write(wb_e_hold + " / " + un_e_hold + " / " + pw_e_hold + "\n")

    # Delete each time we click on the button (to clear the entries)
    wb_e.delete(0, END)
    pw_e.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# first initialize the window to work on
window = Tk()
window.title("My password manager")
window.config(padx=50, pady=50, width=400, height=400)
# create the canevas = import the image.
image_cnv = Canvas(height=200, width=200)
lock = PhotoImage(file="logo.png")
image_cnv.create_image(200 / 2, 189 / 2, image=lock)
image_cnv.grid(row=0, column=1)

# website label
wb_label = Label()
wb_label.config(text="Website")
wb_label.grid(row=1, column=0)
# website entry
wb_e = Entry()
wb_e.focus()
wb_e.config(width=38)
wb_e.grid(row=1, column=1, columnspan=2)
# user name label
un_l = Label()
un_l.config(text="Email/Username")
un_l.grid(row=2, column=0)
# user_name entry
un_e = Entry()
un_e.insert(END, "maxcollet01@gmail.com")
un_e.config(width=38)
un_e.grid(row=2, column=1, columnspan=2)
# password label
pw_l = Label()
pw_l.config(text="Password")
pw_l.grid(row=3, column=0)
# password entry
pw_e = Entry()
pw_e.config(width=21)
pw_e.grid(row=3, column=1)
# password button
pw_b = Button()
pw_b.config(text="Generate Password", command=generate_rand_password)
pw_b.grid(row=3, column=2)
# Add button
add_b = Button()
add_b.config(text="Add", width=36, command=save)
add_b.grid(row=4, column=1, columnspan=2)
# keep the window open with Tkinter
window.mainloop()
