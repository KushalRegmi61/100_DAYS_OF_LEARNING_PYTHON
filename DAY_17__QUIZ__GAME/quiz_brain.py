class QuizBrain:    
    def __init__(self,question_list):
        self.count = 0
        self.qn_no = 0
        self.life = 5
        self.q_list = question_list
        
    def still_has_question(self):
        if self.life > 0 and self.qn_no<len(self.q_list):
            return True
        else:
            return False 
            
    def check_answer(self,user_choice, correct_answer):
        
        if user_choice == correct_answer:
            self.count+= 1
            print(f"Your still have {self.life} life remaining: ")
            print("Congrats!, Your answer is correct \nYoour score is:",self.count,"/",self.qn_no)
        else:
            self.life -= 1
            print(f"Your still have {self.life} life remaining: ")
            print("Opps!, Your answer is wrong \n Your score is:",self.count,"/",self.qn_no)
    
    def next_question(self):
        
        current_qn = self.q_list[self.qn_no]
        self.qn_no +=1 
        choice = input(f"Q.{self.qn_no} {current_qn.text} (True/False)").lower()
        if choice == "t" or choice == "true":
            choice ="True"
        else:
            choice = "False"
        self.check_answer(user_choice=choice, correct_answer= current_qn.answer)
        
    def should_continue(method):
        should_coninue = input("Do you want to start the game?? (Y/N):").lower()
        if should_coninue == "y" or should_coninue == "yes":
            return True
        else :
            return False
            
        
        
        
    
                
    
            

        
    



        
           
