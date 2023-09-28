from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

try:

    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    random_index = 0
    data = pandas.read_csv("data/Hindi Words.csv")
    dict = data.to_dict(orient="records")
else:

    random_index = 0
    dict = data.to_dict(orient="records")



def known():
    dict.remove(dict[random_index])
    new_data = pandas.DataFrame(dict)
    new_data.to_csv("words_to_learn.csv", index=False)
    generate()



def generate():
    canvas.itemconfig(warning, text="Showing translation in 4s")
    global random_index, flip_timer
    window.after_cancel(flip_timer)

    random_index = random.randint(1,1900)
    canvas.itemconfig(show_canvas, image=img_front)
    canvas.itemconfig(title, text="Hindi", fill="black")
    hinglish = dict[random_index]["Transliteration"]
    canvas.itemconfig(word, text=f'{dict[random_index]["Word"]} ({hinglish})', fill="Black")
    flip_timer = window.after(4000, func=flipcard)



def flipcard():
    canvas.itemconfig(warning, text="")
    canvas.itemconfig(show_canvas, image=img_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=f'{dict[random_index]["English_Translation"]}', fill="white")

window = Tk()
window.title("The Flash Card Learn.")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(4000, func=flipcard)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")
show_canvas = canvas.create_image(400, 263, image=img_front)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
button = Button(image=right_image, highlightthickness=0, command=known)
button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
button2 = Button(image=wrong_image, highlightthickness=0, command=generate)
button2.grid(column=0, row=1)

title = canvas.create_text(400, 150, text="Hindi", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
warning = canvas.create_text(400, 400, text="Showing translation in 4s", font=("Ariel", 20))


generate()
window.mainloop()
