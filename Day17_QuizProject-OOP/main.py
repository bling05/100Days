from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dict in question_data:
    question_bank.append(Question(dict["text"], dict["answer"]))
# Creates a list of objects from class Question, called question_bank

quiz = QuizBrain(question_bank)
# Creates a changing object called quiz using class QuizBrain and the question bank

while quiz.still_has_questions():
    quiz.next_question()
# While loop continues asking questions until game is over

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")