from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    with open("data.txt","a") as data_file:
        data_file.write(f"{input_web.get()},{input_user.get()}, {input_pw.get()}")
    input_web.delete(0,END)
    input_user.delete(0,END)
    input_pw.delete(0,END)

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

button_gen = Button(text="Generate Password",highlightthickness=0)
button_gen.grid(row=3,column=2)

button_add = Button(text="Add",highlightthickness=0,width=30,command=save_pw)
button_add.grid(row=4,column=1,columnspan=2)

window.mainloop()