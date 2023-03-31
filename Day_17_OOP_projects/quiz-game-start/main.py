from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for qts in question_data:
    qts_text = qts["text"]
    qts_answer = qts["answer"]
    question_bank.append(Question(qts_text,qts_answer))


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{len(quiz.question_list)}.")

