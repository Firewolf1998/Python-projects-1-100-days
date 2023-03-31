class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_no]
        current_answer = current_question.answer
        self.question_no += 1
        user_answer = input(f"Q{self.question_no}: {current_question.text} (True/False):")
        self.check_answer(user_answer, current_answer)

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def check_answer(self, user_answer, current_answer):

        if user_answer.lower() == current_answer.lower():
            print('You got it right!!!')
            self.score += 1
        else:
            print("Sorry, you got it wrong")
        print(f"Correct answer: {current_answer}.")
        print(f"your score is {self.score}/{self.question_no}")
        print("\n")


