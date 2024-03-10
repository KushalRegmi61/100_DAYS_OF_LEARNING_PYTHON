import random
rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to rock paper and scissor game:")
game = [rock, paper, scissors]
you = ["Rock", "paper", "scissors"]
a= int(input("enter your move: Rock(0), paper(1), scissor(2)"))
c = a
if a >= 3 or a <0:
    print("invalid choice:")
else:
    print("you chose", you[c])
    print(game[a])
    b = random.randint(0,2)
    print("computer choose", you[b])
    print(game[b])
    if a == 0 and b == 1:
        print("you lost:")
    elif a == 0 and b == 2:
        print("you win ")
    elif a == 1 and b ==0:
        print("you win")
    elif a==1 and b == 2:
        print("you lost ")
    elif a == 2 and b == 0:
        print("you lost:")
    elif a == 2 and b == 1:
        print("you won:")
    else:
        print("game is drw:play again") 

i = input()        

