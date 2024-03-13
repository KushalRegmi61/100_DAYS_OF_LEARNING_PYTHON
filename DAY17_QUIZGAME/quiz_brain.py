class QuizBrain:    
    def __init__(self,question_list):
        self.qn_no = 0
        self.q_list = question_list
    
    def next_question(self):
        current_qn = self.q_list[self.qn_no] 
        choice = input(f"Q.{self.qn_no+1} {current_qn.text} (True/False)")
    
    def still_has_question(self):
        return self.qn_no<len(self.q_list)

        
    



        
           
