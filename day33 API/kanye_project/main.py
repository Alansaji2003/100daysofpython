from tkinter import *
import requests

def get_quote():
    responce = requests.get(url="https://api.kanye.rest")
    responce.raise_for_status()
    data = responce.json()
    quote = data["quote"]
    if len(quote) > 50:
        canvas.itemconfig(quote_text, font=("Arial", 15, "bold"))
    else:
        canvas.itemconfig(quote_text, font=("Arial", 30, "bold"))
    canvas.itemconfig(quote_text, text=quote)





window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click on Kanye's head", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye2.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bg="yellow")
kanye_button.grid(row=1, column=0)



window.mainloop()