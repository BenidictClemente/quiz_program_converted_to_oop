class QuizQuestion:
    def __init__(self, question, answers, correct_answer):
        required_keys = {'A', 'B', 'C', 'D'}
        if set(answers.keys()) != required_keys:
            raise ValueError("Answers must include keys: A, B, C, and D")
        correct_answer = correct_answer.upper()
        if correct_answer not in required_keys:
            raise ValueError("Correct answer must be one of A, B, C, or D")

        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    def format_for_file(self):
        formatted = f"Q: {self.question}\n"
        for key in ['A', 'B', 'C', 'D']:
            formatted += f"{key}. {self.answers[key]}\n"
        formatted += f"Correct answer: {self.correct_answer}\n"
        formatted += "***************\n"
        return formatted


class QuizBuilder:
    def __init__(self, filename="quiz_data.txt"):
        self.filename = filename

    def prompt_for_question(self):
        question = input("Enter the question: ")
        answers = {
            'A': input("Enter answer A: "),
            'B': input("Enter answer B: "),
            'C': input("Enter answer C: "),
            'D': input("Enter answer D: "),
        }

        # Validate correct answer input
        while True:
            correct = input("Enter the correct answer (A, B, C, or D): ").strip().upper()
            if correct in answers:
                break
            print("Invalid input. Please enter A, B, C, or D.")

        return QuizQuestion(question, answers, correct)

    def run(self):
        with open(self.filename, "a", encoding="utf-8") as file:
            while True:
                question_obj = self.prompt_for_question()
                file.write(question_obj.format_for_file())
                another = input("Do you want to add another question? (yes/no): ").strip().lower()
                if another != "yes":
                    break
        print(f"Quiz data has been saved to {self.filename}.")


# Run the program
if __name__ == "__main__":
    builder = QuizBuilder()
    builder.run()
