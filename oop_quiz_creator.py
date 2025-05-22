class QuizQuestion:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers  # Dictionary with keys 'A', 'B', 'C', 'D'
        self.correct_answer = correct_answer.upper()

    def format_for_file(self):
        formatted = f"Q: {self.question}\n"
        for key in ['A', 'B', 'C', 'D']:
            formatted += f"{key}. {self.answers[key]}\n"
        formatted += f"Correct answer: {self.correct_answer}\n"
        formatted += "***************\n"
        return formatted