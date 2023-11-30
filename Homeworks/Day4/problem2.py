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

for i in range(6):
    row = []
    for j in range(6):
        row.append("*")
    output.append(row)

points_A = 0
points_B = 0
print("Initial stage:")
print_matrix(output)

def calculate_points(player, matrix, points_A, points_B):
    row = dice() - 1
    col = dice() - 1

    if matrix[row][col] == 'A' and player == 'A':
        print(f"Player A has rolled row={row+1} and col={col+1}.")
        print(f"OOPS! Player A takes Player B's place.")
        points_A += 1
        matrix[row][col] = 'A'
        print_matrix(matrix)
    elif matrix[row][col] == 'B' and player == 'B':
        print(f"Player B has rolled row={row+1} and col={col+1}.")
        print(f"OOPS! Player B takes Player A's place.")
        points_B += 1
        matrix[row][col] = 'B'
        print_matrix(matrix)
    else:
        print(f"Player {player} has rolled row={row+1} and col={col+1}.")
        matrix[row][col] = player
        print_matrix(matrix)

    return points_A, points_B

while points_A < 5 and points_B < 5:
    points_A, points_B = calculate_points('A', output, points_A, points_B)
    points_A, points_B = calculate_points('B', output, points_A, points_B)

print("Game Over!")
print(f"Total points for Player A: {points_A}")
print(f"Total points for Player B: {points_B}")



'''
OUTPUT:-
Initial stage:
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
Player A has rolled row=2 and col=1.
['*', '*', '*', '*', '*', '*']
['A', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
Player B has rolled row=3 and col=6.
['*', '*', '*', '*', '*', '*']
['A', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', 'B']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
Player A has rolled row=1 and col=3.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', 'B']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
Player B has rolled row=4 and col=5.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', 'B']
['*', '*', '*', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
Player A has rolled row=3 and col=2.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', '*', '*', '*']
['*', 'A', '*', '*', '*', 'B']
['*', '*', '*', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
Player B has rolled row=4 and col=3.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', '*', '*', '*']
['*', 'A', '*', '*', '*', 'B']
['*', '*', 'B', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
Player A has rolled row=2 and col=5.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', '*', 'A', '*']
['*', 'A', '*', '*', '*', 'B']
['*', '*', 'B', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
Player B has rolled row=2 and col=4.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', '*']
['*', 'A', '*', '*', '*', 'B']
['*', '*', 'B', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', '*']
Player A has rolled row=6 and col=6.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', '*']
['*', 'A', '*', '*', '*', 'B']
['*', '*', 'B', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', 'A']
Player B has rolled row=2 and col=6.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['*', 'A', '*', '*', '*', 'B']
['*', '*', 'B', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', '*', '*', '*', '*', 'A']
Player A has rolled row=6 and col=2.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['*', 'A', '*', '*', '*', 'B']
['*', '*', 'B', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', 'A', '*', '*', '*', 'A']
Player B has rolled row=3 and col=4.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['*', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', '*', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', 'A', '*', '*', '*', 'A']
Player A has rolled row=4 and col=4.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['*', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', 'A', '*', '*', '*', 'A']
Player B has rolled row=3 and col=1.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', 'A', '*', '*', '*', 'A']
Player A has rolled row=1 and col=3.
OOPS! Player A takes Player B's place.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', 'A', '*', '*', '*', 'A']
Player B has rolled row=3 and col=6.
OOPS! Player B takes Player A's place.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', '*']
['*', 'A', '*', '*', '*', 'A']
Player A has rolled row=5 and col=6.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'A']
['*', 'A', '*', '*', '*', 'A']
Player B has rolled row=6 and col=2.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'A']
['*', 'B', '*', '*', '*', 'A']
Player A has rolled row=2 and col=1.
OOPS! Player A takes Player B's place.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'A']
['*', 'B', '*', '*', '*', 'A']
Player B has rolled row=6 and col=6.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'A']
['*', 'B', '*', '*', '*', 'B']
Player A has rolled row=2 and col=1.
OOPS! Player A takes Player B's place.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'A']
['*', 'B', '*', '*', '*', 'B']
Player B has rolled row=6 and col=2.
OOPS! Player B takes Player A's place.
['*', '*', 'A', '*', '*', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'A']
['*', 'B', '*', '*', '*', 'B']
Player A has rolled row=1 and col=5.
['*', '*', 'A', '*', 'A', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'A']
['*', 'B', '*', '*', '*', 'B']
Player B has rolled row=5 and col=6.
['*', '*', 'A', '*', 'A', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'B']
['*', 'B', '*', '*', '*', 'B']
Player A has rolled row=1 and col=2.
['*', 'A', 'A', '*', 'A', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', '*', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'B']
['*', 'B', '*', '*', '*', 'B']
Player B has rolled row=4 and col=2.
['*', 'A', 'A', '*', 'A', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', '*', 'B']
['*', 'B', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'B']
['*', 'B', '*', '*', '*', 'B']
Player A has rolled row=3 and col=5.
['*', 'A', 'A', '*', 'A', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', 'A', 'B']
['*', 'B', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'B']
['*', 'B', '*', '*', '*', 'B']
Player B has rolled row=3 and col=6.
OOPS! Player B takes Player A's place.
['*', 'A', 'A', '*', 'A', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', 'A', 'B']
['*', 'B', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'B']
['*', 'B', '*', '*', '*', 'B']
Player A has rolled row=5 and col=6.
['*', 'A', 'A', '*', 'A', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', 'A', 'B']
['*', 'B', 'B', 'A', 'B', '*']
['*', '*', '*', '*', '*', 'A']
['*', 'B', '*', '*', '*', 'B']
Player B has rolled row=5 and col=1.
['*', 'A', 'A', '*', 'A', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', 'A', 'B']
['*', 'B', 'B', 'A', 'B', '*']
['B', '*', '*', '*', '*', 'A']
['*', 'B', '*', '*', '*', 'B']
Player A has rolled row=1 and col=4.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'A', 'B']
['B', 'A', '*', 'B', 'A', 'B']
['*', 'B', 'B', 'A', 'B', '*']
['B', '*', '*', '*', '*', 'A']
['*', 'B', '*', '*', '*', 'B']
Player B has rolled row=2 and col=5.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'B', 'B']
['B', 'A', '*', 'B', 'A', 'B']
['*', 'B', 'B', 'A', 'B', '*']
['B', '*', '*', '*', '*', 'A']
['*', 'B', '*', '*', '*', 'B']
Player A has rolled row=5 and col=5.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'B', 'B']
['B', 'A', '*', 'B', 'A', 'B']
['*', 'B', 'B', 'A', 'B', '*']
['B', '*', '*', '*', 'A', 'A']
['*', 'B', '*', '*', '*', 'B']
Player B has rolled row=5 and col=3.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'B', 'B']
['B', 'A', '*', 'B', 'A', 'B']
['*', 'B', 'B', 'A', 'B', '*']
['B', '*', 'B', '*', 'A', 'A']
['*', 'B', '*', '*', '*', 'B']
Player A has rolled row=3 and col=4.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'B', 'B']
['B', 'A', '*', 'A', 'A', 'B']
['*', 'B', 'B', 'A', 'B', '*']
['B', '*', 'B', '*', 'A', 'A']
['*', 'B', '*', '*', '*', 'B']
Player B has rolled row=6 and col=1.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'B', 'B']
['B', 'A', '*', 'A', 'A', 'B']
['*', 'B', 'B', 'A', 'B', '*']
['B', '*', 'B', '*', 'A', 'A']
['B', 'B', '*', '*', '*', 'B']
Player A has rolled row=4 and col=6.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'B', 'B']
['B', 'A', '*', 'A', 'A', 'B']
['*', 'B', 'B', 'A', 'B', 'A']
['B', '*', 'B', '*', 'A', 'A']
['B', 'B', '*', '*', '*', 'B']
Player B has rolled row=5 and col=6.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'B', 'B']
['B', 'A', '*', 'A', 'A', 'B']
['*', 'B', 'B', 'A', 'B', 'A']
['B', '*', 'B', '*', 'A', 'B']
['B', 'B', '*', '*', '*', 'B']
Player A has rolled row=4 and col=6.
OOPS! Player A takes Player B's place.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'B', 'B']
['B', 'A', '*', 'A', 'A', 'B']
['*', 'B', 'B', 'A', 'B', 'A']
['B', '*', 'B', '*', 'A', 'B']
['B', 'B', '*', '*', '*', 'B']
Player B has rolled row=6 and col=3.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'B', 'B']
['B', 'A', '*', 'A', 'A', 'B']
['*', 'B', 'B', 'A', 'B', 'A']
['B', '*', 'B', '*', 'A', 'B']
['B', 'B', 'B', '*', '*', 'B']
Player A has rolled row=1 and col=2.
OOPS! Player A takes Player B's place.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'B', 'B']
['B', 'A', '*', 'A', 'A', 'B']
['*', 'B', 'B', 'A', 'B', 'A']
['B', '*', 'B', '*', 'A', 'B']
['B', 'B', 'B', '*', '*', 'B']
Player B has rolled row=6 and col=5.
['*', 'A', 'A', 'A', 'A', '*']
['A', '*', '*', 'B', 'B', 'B']
['B', 'A', '*', 'A', 'A', 'B']
['*', 'B', 'B', 'A', 'B', 'A']
['B', '*', 'B', '*', 'A', 'B']
['B', 'B', 'B', '*', 'B', 'B']
Game Over!
Total points for Player A: 5
Total points for Player B: 3
'''
