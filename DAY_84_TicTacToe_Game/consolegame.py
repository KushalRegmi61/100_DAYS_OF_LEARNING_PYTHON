import random

def printboard(x_state, o_state):
    zero = 'X' if x_state[0] else 'O' if o_state[0] else ' ';
    one = 'X' if x_state[1] else 'O' if o_state[1] else ' ';
    two = 'X' if x_state[2] else 'O' if o_state[2] else ' ';
    three = 'X' if x_state[3] else 'O' if o_state[3] else ' ';
    four = 'X' if x_state[4] else 'O' if o_state[4] else ' ';
    five = 'X' if x_state[5] else 'O' if o_state[5] else ' ';
    six = 'X' if x_state[6] else 'O' if o_state[6] else ' ';
    seven = 'X' if x_state[7] else 'O' if o_state[7] else ' ';
    eight = 'X' if x_state[8] else 'O' if o_state[8] else ' ';

   #printting board 
    print(f"{zero} | {one} | {two}")
    print("---------")
    print(f"{three} | {four} | {five}")
    print("---------")
    print(f"{six} | {seven} | {eight}")


#sum function
def sum(a,b,c):
    return a+b+c

#check for winner
def check_winner(x_state, o_state):
    winning_list = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

        #checking if x wins
    for i in winning_list:
            if sum(x_state[i[0]], x_state[i[1]], x_state[i[2]]) == 3:
                print("X wins")
                printboard(x_state, o_state)
                return 1
        #checking if o wins
            if sum(o_state[i[0]], o_state[i[1]], o_state[i[2]]) == 3:
                print("O wins")
                printboard(x_state, o_state)
                return 0
            
    return -1



if  __name__ == '__main__':
    user_move = 0
    #To choose between and the player and the computer
    player_choice =int(input("Do you want to play with computer or with another player?\n  (1-Computer / 0 - Other player): "))
    tie=0 #checking the condition for tie
    turn = random.randint(0,1)# 1 for X_turn and 0 for O_turn
    x_state = [0,0,0,0,0,0,0,0,0]
    o_state = [0,0,0,0,0,0,0,0,0]
    computer_move = [0,1,2,3,4,5,6,7,8]
    while True:
        printboard(x_state, o_state)
        if turn:
            print("X's turn")
            move = int(input("Enter your move: "))
            user_move = move
            computer_move.remove(user_move)
            if x_state[move] or o_state[move]:
                print("Invalid move")
                continue
            x_state[move] = 1
            
        else:
            # O's turn other player
            if player_choice ==0:
                print("O's turn")
                move = int(input("Enter your move: "))

            # O's turn computer
            else :
                print("Computer's turn")
                move = random.choice(computer_move)
                computer_move.remove(move)
                print(f"Computer's move: {move}")

            if x_state[move] or o_state[move]:
                print("Invalid move")
                continue
            o_state[move] = 1

        turn = 1 - turn
        tie = tie+1 #incrementing the tie

        #check for winner
        winner = check_winner(x_state, o_state)
        if winner != -1 :
            print("Game Over")
            break

        elif tie == 9:
            print("Game Tied")
            break
      
            