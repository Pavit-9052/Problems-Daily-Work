'''
Problem #2
You have 6 x 6 game board where each cell is shown as a *
This is a two player dice game. The die has numbers 1 to 6.
Each player rolls the dice twice. First roll is row number, second roll is col number.
After the player rolls the dice, in the (row,col) enter the player's initial. 
If the player  A rolls the dice and  if  player B already has their initial in the same row,col
add a point to A and change the initial to A. 

Player who gets 5 points first wins the game.
Print the board each time after the user rolls and also print the current score.
Use functions
'''


import random

def dice():
    random_number = random.randint(1, 6)
    return random_number

def print_matrix(matrix):
    for row in matrix:
        print(row)

output = []

for i in range(6):      #To create a 6x6 dimensional array
    row = []
    for j in range(6):
        row.append("*")
    output.append(row)

points_A = 0
points_B = 0
print("Initial stage:")
print_matrix(output)

while points_A < 5 and points_B < 5: #To iterate until the point is 5 when game ends!
    for i in range(1, 3):
        row = dice() - 1
        col = dice() - 1
        if i == 1:  #Player A's turn
            if output[row][col] == 'B':
                print(f"Player A has rolled row={row+1} and col={col+1}.")
                print(f"OOPS! Player A takes Player B's place.")
                points_A += 1
                output[row][col] = 'A'
                print_matrix(output)
            else:
                print(f"Player A has rolled row={row+1} and col={col+1}.")
                output[row][col] = 'A'
                print_matrix(output)
        else:      #Player B's turn
            if output[row][col] == 'A':
                print(f"Player B has rolled row={row+1} and col={col+1}.")
                print(f"OOPS! Player B takes Player A's place.")
                points_B += 1
                output[row][col] = 'B'
                print_matrix(output)
            else:
                print(f"Player B has rolled row={row+1} and col={col+1}.")
                output[row][col] = 'B'
                print_matrix(output)

    print(f"Total points for Player A: {points_A}")
    print(f"Total points for Player B: {points_B}")

    if points_A >= 5 or points_B >= 5:
        break




'''
OUTPUT:-
Initial stage:
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
Player A has rolled row=1 and col=2.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
Player B has rolled row=5 and col=6.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', 'B']
['*', '*', '*', '*', '*', '*']
Total points for Player A: 0
Total points for Player B: 0
Player A has rolled row=1 and col=2.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', 'B']
['*', '*', '*', '*', '*', '*']
Player B has rolled row=3 and col=5.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', 'B']
['*', '*', '*', '*', '*', '*']
Total points for Player A: 0
Total points for Player B: 0
Player A has rolled row=6 and col=3.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', 'B']
['*', '*', 'A', '*', '*', '*']
Player B has rolled row=5 and col=2.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', 'B', '*', '*', '*', 'B']
['*', '*', 'A', '*', '*', '*']
Total points for Player A: 0
Total points for Player B: 0
Player A has rolled row=3 and col=4.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', 'B', '*', '*', '*', 'B']
['*', '*', 'A', '*', '*', '*']
Player B has rolled row=2 and col=4.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', 'B', '*', '*']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', 'B', '*', '*', '*', 'B']
['*', '*', 'A', '*', '*', '*']
Total points for Player A: 0
Total points for Player B: 0
Player A has rolled row=6 and col=3.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', 'B', '*', '*']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', 'B', '*', '*', '*', 'B']
['*', '*', 'A', '*', '*', '*']
Player B has rolled row=5 and col=3.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', 'B', '*', '*']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', '*', '*', '*']
Total points for Player A: 0
Total points for Player B: 0
Player A has rolled row=5 and col=1.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', 'B', '*', '*']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', '*', '*', '*']
Player B has rolled row=6 and col=4.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', 'B', '*', '*']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', '*', '*']
Total points for Player A: 0
Total points for Player B: 0
Player A has rolled row=6 and col=4.
OOPS! Player A takes Player B's place.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', 'B', '*', '*']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'A', '*', '*']
Player B has rolled row=2 and col=6.
['*', 'A', '*', '*', '*', '*']
['*', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'A', '*', '*']
Total points for Player A: 1
Total points for Player B: 0
Player A has rolled row=1 and col=6.
['*', 'A', '*', '*', '*', 'A']
['*', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'A', '*', '*']
Player B has rolled row=6 and col=4.
OOPS! Player B takes Player A's place.
['*', 'A', '*', '*', '*', 'A']
['*', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', '*', '*']
Total points for Player A: 1
Total points for Player B: 1
Player A has rolled row=2 and col=1.
['*', 'A', '*', '*', '*', 'A']
['A', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', '*', '*']
Player B has rolled row=1 and col=5.
['*', 'A', '*', '*', 'B', 'A']
['A', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', '*', '*']
Total points for Player A: 1
Total points for Player B: 1
Player A has rolled row=2 and col=1.
['*', 'A', '*', '*', 'B', 'A']
['A', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', '*', '*']
Player B has rolled row=6 and col=5.
['*', 'A', '*', '*', 'B', 'A']
['A', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', 'B', '*']
Total points for Player A: 1
Total points for Player B: 1
Player A has rolled row=3 and col=6.
['*', 'A', '*', '*', 'B', 'A']
['A', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', 'B', '*']
Player B has rolled row=1 and col=4.
['*', 'A', '*', 'B', 'B', 'A']
['A', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', 'B', '*']
Total points for Player A: 1
Total points for Player B: 1
Player A has rolled row=6 and col=6.
['*', 'A', '*', 'B', 'B', 'A']
['A', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', 'B', 'A']
Player B has rolled row=1 and col=1.
['B', 'A', '*', 'B', 'B', 'A']
['A', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', 'B', 'A']
Total points for Player A: 1
Total points for Player B: 1
Player A has rolled row=6 and col=3.
['B', 'A', '*', 'B', 'B', 'A']
['A', '*', '*', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', 'B', 'A']
Player B has rolled row=2 and col=3.
['B', 'A', '*', 'B', 'B', 'A']
['A', '*', 'B', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', '*', '*', 'B']
['*', '*', 'A', 'B', 'B', 'A']
Total points for Player A: 1
Total points for Player B: 1
Player A has rolled row=5 and col=4.
['B', 'A', '*', 'B', 'B', 'A']
['A', '*', 'B', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', 'A', '*', 'B']
['*', '*', 'A', 'B', 'B', 'A']
Player B has rolled row=6 and col=1.
['B', 'A', '*', 'B', 'B', 'A']
['A', '*', 'B', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', 'A', '*', 'B']
['B', '*', 'A', 'B', 'B', 'A']
Total points for Player A: 1
Total points for Player B: 1
Player A has rolled row=5 and col=5.
['B', 'A', '*', 'B', 'B', 'A']
['A', '*', 'B', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', 'A', 'A', 'B']
['B', '*', 'A', 'B', 'B', 'A']
Player B has rolled row=5 and col=4.
OOPS! Player B takes Player A's place.
['B', 'A', '*', 'B', 'B', 'A']
['A', '*', 'B', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['*', '*', '*', '*', '*', '*']
['A', 'B', 'B', 'B', 'A', 'B']
['B', '*', 'A', 'B', 'B', 'A']
Total points for Player A: 1
Total points for Player B: 2
Player A has rolled row=4 and col=1.
['B', 'A', '*', 'B', 'B', 'A']
['A', '*', 'B', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['A', '*', '*', '*', '*', '*']
['A', 'B', 'B', 'B', 'A', 'B']
['B', '*', 'A', 'B', 'B', 'A']
Player B has rolled row=6 and col=3.
OOPS! Player B takes Player A's place.
['B', 'A', '*', 'B', 'B', 'A']
['A', '*', 'B', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['A', '*', '*', '*', '*', '*']
['A', 'B', 'B', 'B', 'A', 'B']
['B', '*', 'B', 'B', 'B', 'A']
Total points for Player A: 1
Total points for Player B: 3
Player A has rolled row=4 and col=5.
['B', 'A', '*', 'B', 'B', 'A']
['A', '*', 'B', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['A', '*', '*', '*', 'A', '*']
['A', 'B', 'B', 'B', 'A', 'B']
['B', '*', 'B', 'B', 'B', 'A']
Player B has rolled row=2 and col=6.
['B', 'A', '*', 'B', 'B', 'A']
['A', '*', 'B', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['A', '*', '*', '*', 'A', '*']
['A', 'B', 'B', 'B', 'A', 'B']
['B', '*', 'B', 'B', 'B', 'A']
Total points for Player A: 1
Total points for Player B: 3
Player A has rolled row=2 and col=2.
['B', 'A', '*', 'B', 'B', 'A']
['A', 'A', 'B', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['A', '*', '*', '*', 'A', '*']
['A', 'B', 'B', 'B', 'A', 'B']
['B', '*', 'B', 'B', 'B', 'A']
Player B has rolled row=2 and col=6.
['B', 'A', '*', 'B', 'B', 'A']
['A', 'A', 'B', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['A', '*', '*', '*', 'A', '*']
['A', 'B', 'B', 'B', 'A', 'B']
['B', '*', 'B', 'B', 'B', 'A']
Total points for Player A: 1
Total points for Player B: 3
Player A has rolled row=2 and col=3.
OOPS! Player A takes Player B's place.
['B', 'A', '*', 'B', 'B', 'A']
['A', 'A', 'A', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['A', '*', '*', '*', 'A', '*']
['A', 'B', 'B', 'B', 'A', 'B']
['B', '*', 'B', 'B', 'B', 'A']
Player B has rolled row=6 and col=6.
OOPS! Player B takes Player A's place.
['B', 'A', '*', 'B', 'B', 'A']
['A', 'A', 'A', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['A', '*', '*', '*', 'A', '*']
['A', 'B', 'B', 'B', 'A', 'B']
['B', '*', 'B', 'B', 'B', 'B']
Total points for Player A: 2
Total points for Player B: 4
Player A has rolled row=2 and col=3.
['B', 'A', '*', 'B', 'B', 'A']
['A', 'A', 'A', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['A', '*', '*', '*', 'A', '*']
['A', 'B', 'B', 'B', 'A', 'B']
['B', '*', 'B', 'B', 'B', 'B']
Player B has rolled row=1 and col=6.
OOPS! Player B takes Player A's place.
['B', 'A', '*', 'B', 'B', 'B']
['A', 'A', 'A', 'B', '*', 'B']
['*', '*', '*', 'A', 'B', 'A']
['A', '*', '*', '*', 'A', '*']
['A', 'B', 'B', 'B', 'A', 'B']
['B', '*', 'B', 'B', 'B', 'B']
Total points for Player A: 2
Total points for Player B: 5
'''
