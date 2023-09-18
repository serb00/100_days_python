from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []


def init_question_bank():
    global question_bank
    for item in question_data:
        question_bank.append(Question(item["text"], item["answer"]))


def main():
    init_question_bank()
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    quiz.display_final_score()

if __name__ == "__main__":
    main()
