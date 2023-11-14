from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_BG_COLOR = "#323232"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.lb_score = Label(text="Score: 0", background=THEME_COLOR)
        self.lb_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg=CANVAS_BG_COLOR, highlightthickness=0)
        self.txt_question = self.canvas.create_text(
            150, 125,
            fill="white",
            width=280,
            font=("Arial", 20, "italic"),
            text="Some question text...")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        img_true = PhotoImage(file="./images/true.png")
        self.btn_true = Button(image=img_true, borderwidth=0, command=self.btn_true_pressed)
        self.btn_true.grid(row=2, column=0)
        img_false = PhotoImage(file="./images/false.png")
        self.btn_false = Button(image=img_false, borderwidth=0, command=self.btn_false_pressed)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background=CANVAS_BG_COLOR)
        self.lb_score.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.txt_question, text=q_text)
        else:
            self.canvas.config(background=CANVAS_BG_COLOR)
            self.canvas.itemconfig(
                self.txt_question,
                text=f"You have completed the quiz!\n\nYour Score is {self.quiz.score}/{self.quiz.question_number}")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def btn_true_pressed(self):
        answer_correct = self.quiz.check_answer("True")
        self.feedback_to_user(answer_correct)

    def btn_false_pressed(self):
        answer_correct = self.quiz.check_answer("False")
        self.feedback_to_user(answer_correct)

    def feedback_to_user(self, correct):
        if correct:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, func=self.get_next_question)
