from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = ([random.choice(letters) for _ in range(random.randint(8, 10))] +
                     [random.choice(symbols) for _ in range(random.randint(2, 4))] +
                     [random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def restore_entries():
    entry_website.delete(0, END)
    entry_password.delete(0, END)
    entry_website.focus()


def validate_entries():
    if (len(entry_website.get()) > 2 and
            len(entry_username.get()) > 2 and
            len(entry_password.get()) > 2):
        return True
    else:
        return False


def add_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if not validate_entries():
        messagebox.showerror(title="Validation error", message="Please enter correct data.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"""You're doing to add this to database.
Username: {username}
Password: {password}
Please press OK to add.""")

    if is_ok:
        with open("passwords.txt", mode="a") as file:
            file.write(f"{website}|{username}|{password}\n")
        restore_entries()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)
img_lock = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img_lock)
canvas.grid(row=0, column=1)

# Labels
lbl_website = Label(text="Website:")
lbl_website.grid(row=1, column=0)

lbl_username = Label(text="Email/Username:")
lbl_username.grid(row=2, column=0)

lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0)

# Entries
entry_website = Entry(width=38)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_username = Entry(width=38)
entry_username.grid(row=2, column=1, columnspan=2)
entry_username.insert(0, "sergei@gmail.com")

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)

# Buttons

btn_generate_pass = Button(text="Generate password", command=generate_password)
btn_generate_pass.grid(row=3, column=2)

btn_add_pass = Button(text="Add password", width=36, command=add_password)
btn_add_pass.grid(row=4, column=1, columnspan=2)

window.mainloop()
