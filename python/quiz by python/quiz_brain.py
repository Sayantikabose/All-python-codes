class QuizBrain():
    def __init__(self,question_list):
        self.question_no=0
        self.question_list= question_list 
        self.score=0
    
    def still_has_questions(self):
        if(self.question_no<len(self.question_list)):
            return False
        else:
            return True
    
    def check_answer(self,user_answer,correct_answer): 
        a=self.question_no+1
        if(user_answer== correct_answer):
            print("That's correct") 
            self.score=self.score+1 
            print(f"The correct answer is {correct_answer}") 
            print(f"Your score is {self.score}/{a}")
        else:
            print("That's incorrect") 
            print(f"The correct answer is {correct_answer}") 
            print(f"Your score is {self.score}/{a}")


    def nextQuestion(self):
        current_question=self.question_list[self.question_no] 
        q_no=self.question_no+1
        user_ans=input(f"Q.{q_no}:{current_question.text} (True/False)")
        self.check_answer(user_ans,current_question.answer)
    
    