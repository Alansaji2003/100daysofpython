from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# making question bank of question objects through for loop
for i in question_data:
    q = Question(i["text"], i["answer"])
    question_bank.append(q)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print("Your current score is ", quiz.score, "/", quiz.question_number)
    print("\n")

print("Your score was", quiz.score)
