class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {question.text} (True/False)")
        self.check_answer(choice, question.answer)

    def check_answer(self, user_choice, correct_answer):
        if user_choice.lower() == correct_answer.lower():
            self.score += 1
            print("you were right!!")
        else:
            print("AHH you were wrong")




