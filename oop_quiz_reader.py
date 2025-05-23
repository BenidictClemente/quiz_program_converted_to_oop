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
            question = lines[0][3:].strip() if lines[0].startswith("Q:") else lines[0].strip()
            answers = {
                'A': lines[1][2:].strip(),
                'B': lines[2][2:].strip(),
                'C': lines[3][2:].strip(),
                'D': lines[4][2:].strip(),
            }
            correct_line = lines[5]
            if "Correct answer:" in correct_line:
                correct_answer = correct_line.split(":")[1].strip().upper()
                self.questions.append(QuizQuestion(question, answers, correct_answer))

    def start(self):
        if not self.questions:
            print("No questions available.")
            return

        selected_questions = random.sample(self.questions, min(self.max_questions, len(self.questions)))
        score = 0

        for i, question in enumerate(selected_questions, 1):
            question.display(i)
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            if question.is_correct(user_answer):
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. Correct answer is: {question.correct_answer}")

        print(f"\nFinal score: {score}/{len(selected_questions)}")


# Run the game
if __name__ == "__main__":
    game = QuizGame()
    game.load_questions()
    game.start()