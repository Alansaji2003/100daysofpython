from tkinter import *  # This only imports all classes, message box is a module
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generatePassword():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(6, 8))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letter
    shuffle(password_list)

    password = "".join(password_list)


    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(website_entry.get()) == 0:
        messagebox.askokcancel(title="Empty Fields!",
                               message="The website field is empty, Fill in the appropriate details before adding.")
    elif len(password_entry.get()) == 0:
        messagebox.askokcancel(title="Empty Fields!",
                               message="The Password field is empty, Fill in the appropriate details before adding.")
    elif len(email_entry.get()) == 0:
        messagebox.askokcancel(title="Empty Fields!",
                               message="The email field is empty, Fill in the appropriate details before adding.")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"Details Recieved...\n email: {email_entry.get()}\n Password:"
                                               f" {password_entry.get()}\n Save?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(website_entry.get() + "  |  " + email_entry.get() + "  |  " + password_entry.get() + "\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Success", message="Saved successfully in data.txt file.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Alan's Password Manager")
window.config(padx=70, pady=70)

canvas = Canvas(width=220, height=220)
icon = PhotoImage(file="secure-icon-png-4980.png")
canvas.create_image(110, 110, image=icon)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, columnspan=2, column=1)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, "alan.saji2021@vitbhopal.ac.in")
email_entry.grid(row=2, columnspan=2, column=1)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=16)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password:",  command=generatePassword)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, height=1, command=save,bg="#6cd5e0")
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
