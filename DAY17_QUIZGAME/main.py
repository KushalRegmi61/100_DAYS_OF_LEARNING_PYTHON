from data import question_data
from question_model import Question
question_bank = []
for i in question_data:
    Text = i["text"]
    Answer = i["answer"]
    question_bank.append( Question(Text, Answer))
from quiz_brain import QuizBrain        
quiz = QuizBrain(question_bank)
score =0
# print("hello world")
# while quiz.still_has_question:
#     print(quiz.next_question())       
#     quiz.qn_no +=1 
    
    