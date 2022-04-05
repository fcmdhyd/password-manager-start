from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    input_pw.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    website = input_web.get()
    email = input_user.get()
    password = input_pw.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops~", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \n\nEmail: {email} "
                                                     f"\nPassword: {password} \n\nIs it okay to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}, {email}, {password}\n")
            input_web.delete(0, END)
            input_pw.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_png)
canvas.grid(row=0,column=1)

website = Label(text="Website: ", font=("Arial",10))
website.grid(row=1, column=0)

input_web = Entry(width=35)
input_web.grid(row=1, column=1, columnspan=2)
input_web.focus()

email_user = Label(text="Email/Username: ", font=("Arial",10))
email_user.grid(row=2, column=0)

input_user = Entry(width=35)
input_user.grid(row=2, column=1, columnspan=2)
input_user.insert(0,"fcmdhyd@gmail.com")

password = Label(text="Password: ", font=("Arial",10))
password.grid(row=3, column=0)

input_pw = Entry(width=21)
input_pw.grid(row=3, column=1)

button_gen = Button(text="Generate Password",highlightthickness=0,command=generate_password)
button_gen.grid(row=3,column=2)

button_add = Button(text="Add",highlightthickness=0,width=30,command=save_pw)
button_add.grid(row=4,column=1,columnspan=2)

window.mainloop()