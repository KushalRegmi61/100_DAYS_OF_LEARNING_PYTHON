from data import question_data
from question_model import Question
question_bank = []
for i in question_data:
    Text = i["text"]
    Answer = i["answer"]
    question_bank.append( Question(Text, Answer))
from quiz_brain import QuizBrain        
quiz = QuizBrain(question_bank)
while quiz.should_continue():
    while quiz.still_has_question():       
        quiz.next_question()

    print("\n\nYour Quiz_game is completed")    
    print(f"\nYour final score is {quiz.count}/{quiz.qn_no}")    
            