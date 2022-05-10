class Quiz:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
    
    def remaining_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
            print("Awesome, you got it right!")
        else:
            print("Oops, you got it wrong!")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
