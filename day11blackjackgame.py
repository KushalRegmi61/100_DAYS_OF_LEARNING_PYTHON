import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def comp():
   cond = True
   a = 0
   b = 0 
   compchoice = random.sample(cards, random.randint(2,3))
   for i in compchoice:
       a += i
   your_choice = random.sample(cards, 2) 
   for j in your_choice:
       b += j        
   print("your cards:\t", your_choice, "sum:\t", b)
   if b > 10:
           cards[0] = 1
   while cond:
        print("computer 1st card", compchoice[0])   
        c = input("do you want to continue(Y/N):")
        if c == "N" or c =="n":
            cond = False
        else:
            new_choice = random.choice(cards)
            your_choice.append(new_choice)
            b += new_choice
            
            if b >21 :
                print("you loose the game:")
                print(your_choice,"sum:\t",b)
                cond = False
            else:
                print("cards \t", your_choice, "sum", b)        
   if a > 21:
           print("YOU are the winner", your_choice, b,"\ncomputer choice", compchoice,a)
           
   elif b>a and b <22:
        print("YOU are the winner", your_choice, b,"\ncomputer choice", compchoice,a)
   elif b ==a:
       print("drwa")
   else:
        print("computer is the winner", your_choice, b, "\ncomputer choice", compchoice,a)
cond2 = True
while cond2:
    comp()
    e = input("do you want to continue/restart the game?")
    if e == "n":
        cond2 = False            
         
                
        
            
       
        

    
    