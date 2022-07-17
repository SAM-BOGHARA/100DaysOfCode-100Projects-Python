class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_num < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(
            f"Q.{self.question_num}: {current_question.text} (True/False):").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You didn't get it right!")
        print(f"The correct answer was : {correct_answer}")
        print(f"Score: {(self.score)}/{(self.question_num)}")
        print("\n")
        print("================================")
        print("\n")
