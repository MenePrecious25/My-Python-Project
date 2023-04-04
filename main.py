from data import question_data
from questions_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
percentage_score = (quiz.score/len(question_bank)) * 100
percentage_score = int(percentage_score)
if percentage_score > 70:
    print("Congratulations: You Passed the quiz")
    print(f"Your final score was: {percentage_score}%")
else:
    print("Try Again!!! Your score was below 70%")
    print(f"Your final score was: {percentage_score}%")
