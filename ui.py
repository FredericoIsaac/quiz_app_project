from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 15, "normal")
        )
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=FONT
        )

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_answer)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_answer)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
