from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
ALL_WORDS_CSV = "data/french_words.csv"
WORDS_TO_LEARN = "data/words_to_learn.csv"
DELAY = 3000
CARD_FROM = "French"
CARD_TO = "English"

current_card = {}


# ------------------- SAVE / LOAD ----------------------------#
def load_whole_list():
    global to_learn
    df = pandas.read_csv(ALL_WORDS_CSV)
    to_learn = df.to_dict(orient="records")


def load_data():
    global to_learn
    try:
        df = pandas.read_csv(WORDS_TO_LEARN)
    except FileNotFoundError:
        df = pandas.read_csv(ALL_WORDS_CSV)

    return df.to_dict(orient="records")


def save_data():
    global to_learn
    df = pandas.DataFrame(to_learn)
    df.to_csv(WORDS_TO_LEARN, index=False)


# ------------------ DATA ------------------------------------#

def remove_word():
    global current_card, to_learn
    to_learn.remove(current_card)
    save_data()
    next_card()


def next_card():
    global timer, current_card
    window.after_cancel(timer)
    if len(to_learn) > 0:
        current_card = random.choice(to_learn)
        canvas.itemconfig(img_card, image=img_card_front)
        canvas.itemconfig(txt_title, text=CARD_FROM, fill="black")
        canvas.itemconfig(txt_word, text=current_card[CARD_FROM], fill="black")
        timer = window.after(DELAY, func=reveal_card)
    else:
        load_whole_list()
        next_card()


def reveal_card():
    canvas.itemconfig(img_card, image=img_card_back)
    canvas.itemconfig(txt_title, text=CARD_TO, fill="white")
    canvas.itemconfig(txt_word, text=current_card[CARD_TO], fill="white")


# ------------------ UI ------------------------------------#
to_learn = load_data()

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Flashy")
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
img_card_front = PhotoImage(file="./images/card_front.png")
img_card_back = PhotoImage(file="images/card_back.png")
img_card = canvas.create_image(400, 263, image=img_card_front)
txt_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
txt_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

img_wrong = PhotoImage(file="./images/wrong.png")
btn_wrong = Button(image=img_wrong, highlightthickness=0, border=0, command=next_card)
btn_wrong.grid(row=1, column=0)
img_right = PhotoImage(file="./images/right.png")
btn_right = Button(image=img_right, highlightthickness=0, border=0, command=remove_word)
btn_right.grid(row=1, column=1)

timer = window.after(DELAY, func=reveal_card)
next_card()

window.mainloop()
