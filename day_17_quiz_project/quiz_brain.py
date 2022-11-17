class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
        self.question_number += 1
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("\n")
            print("You got it right!")
        else:
            print("\n")
            print("That's wrong.")

        print(f"The correct answer is {correct_answer}.")
        print(f"Your score is: {self.score}/{(self.question_number)} ")
        print("\n")

    def final_score(self):
        print("You've completed the quiz. ")
        print(f"Your final score was {self.score}/{self.question_number}.")