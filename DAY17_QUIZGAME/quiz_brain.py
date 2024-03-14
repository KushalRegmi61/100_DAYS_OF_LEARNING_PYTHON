class QuizBrain:    
    def __init__(self,question_list):
        self.count = 0
        self.qn_no = 0
        self.q_list = question_list
        
    def still_has_question(self):
        return self.qn_no<len(self.q_list)
            
    def check_answer(self,user_choice, correct_answer):
        
        if user_choice == correct_answer.lower():
            self.count+= 1
            print("Congrats!, Your answer is correct \nYoour score is:",self.count,"/",self.qn_no+1)
        else:
            print("Opps!, Your answer is wrong \n Your score is:",self.count,"/",self.qn_no+1)
    
    def next_question(self):
        
        current_qn = self.q_list[self.qn_no]
        self.qn_no +=1 
        choice = input(f"Q.{self.qn_no} {current_qn.text} (True/False)").lower()
        self.check_answer(user_choice=choice, correct_answer= current_qn.answer)
        
    
                
    
            

        
    



        
           
