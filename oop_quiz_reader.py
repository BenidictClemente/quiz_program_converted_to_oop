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