from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9BDEAC"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer: str = ""


# ------------------------- General functions ----------------------------- #
def change_lb_main(text, color):
    lb_main.config(text=text, fg=color)


def increase_reps():
    global reps
    reps += 1
    if reps % 8 == 0:
        new_text = "✓✓✓✓ 👍"
    else:
        cur_work_rounds, _ = divmod(reps % 8, 2)
        new_text = "✓" * cur_work_rounds
    lb_rounds.config(text=new_text)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    change_lb_main("Timer", GREEN)
    reps = 0
    lb_rounds.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    increase_reps()

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_seconds)
        change_lb_main("Break", RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        change_lb_main("Break", PINK)
    else:
        count_down(work_seconds)
        change_lb_main("Work", GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    minutes, seconds = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{minutes:0>2}:{seconds:0>2}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
lb_main = Label(text="Timer", font=(FONT_NAME, 35, ""), fg=GREEN, bg=YELLOW)
lb_main.grid(row=0, column=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons
btn_start = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
btn_start.grid(row=2, column=0)

btn_reset = Button(text="Reset", command=reset_timer, highlightbackground=YELLOW)
btn_reset.grid(row=2, column=2)

# Label showing rounds
lb_rounds = Label(text="", font=(FONT_NAME, 35, ""), fg=GREEN, bg=YELLOW)
lb_rounds.grid(row=3, column=1)

window.mainloop()
