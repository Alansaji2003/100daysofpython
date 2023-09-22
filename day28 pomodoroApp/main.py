from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF007F"
RED = "#e7305b"
GREEN = "#558427"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- APPEAR ON TOP------------------------------- #

def raise_above_all():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_txt, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    reps += 1
    worksec = WORK_MIN * 60
    shortbreaksec = SHORT_BREAK_MIN * 60
    longbreaksec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(longbreaksec)
        label.config(text="Take a Break", fg=RED)
        raise_above_all()
    elif reps % 2 == 0:
        count_down(shortbreaksec)
        label.config(text="Take a Break", fg=PINK)
        raise_above_all()
    else:
        count_down(worksec)
        label.config(text="Time to Work")
        raise_above_all()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        startTimer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✓"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=50, pady=30, bg=YELLOW)

canvas = Canvas(width=554, height=530, bg=YELLOW)
tomato = PhotoImage(file="tomato-png-16712.png")
canvas.create_image(280, 265, image=tomato)
timer_txt = canvas.create_text(280, 295, text="00:00", fill="white", font=(FONT_NAME, 65, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", background=YELLOW, font=(FONT_NAME, 37, "bold"), fg=GREEN)
# label.place(x=200, y=-60)
label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 17, "bold"), fg=GREEN, command=startTimer)
# start_button.place(x=0, y=500)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 17, "bold"), fg=GREEN, command=reset)
# reset_button.place(x=490, y=490)
reset_button.grid(column=2, row=2)

check_label = Label(font=(FONT_NAME, 37, "bold"), bg=YELLOW, fg=GREEN)
# check_label.place(x=245, y=540)
check_label.grid(column=1, row=3)

window.mainloop()
