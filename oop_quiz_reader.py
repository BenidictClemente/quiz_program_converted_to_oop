import random

class QuizQuestion:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers  # Dictionary: {'A': ..., 'B': ..., 'C': ..., 'D': ...}
        self.correct_answer = correct_answer.upper()

    def display(self, number):
        print(f"\nQuestion {number}: {self.question}")
        for key in ['A', 'B', 'C', 'D']:
            print(f"{key}: {self.answers[key]}")

    def is_correct(self, user_answer):
        return user_answer.upper() == self.correct_answer
class QuizGame:
    def __init__(self, filename="quiz_data.txt", max_questions=20):
        self.filename = filename
        self.max_questions = max_questions
        self.questions = []

    def load_questions(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            raw_data = file.read()

        blocks = raw_data.strip().split("***************")
        for block in blocks:
            lines = block.strip().split("\n")
            if len(lines) < 6:
                continue