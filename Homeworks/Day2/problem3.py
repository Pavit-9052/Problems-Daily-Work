'''
Problem #3
Its is a single player game where the user starts with 0 points. User keeps rolling the 
dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
 added. If the number is odd, then if the number is 1,3 then the user has to jump. 
 If the number is 5, then 3 points are added. The game ends when the user has 50 points.
 '''

import random

def dice_roll():
    return random.randint(0, 6)
points = 0
while points <= 50:
    number = dice_roll()

    if number == 0:
        print("Game Over! You rolled a 0.")
        break
    elif number % 2 == 0:
        points += 2
        print(f"You rolled {number}. You gained 2 points. Total points: {points}")
    elif number in [1, 3]:
        print(f"You rolled {number}. You have to jump!")
    elif number == 5:
        points += 3
        print(f"You rolled 5. You gained 3 points. Total points: {points}")

if points >= 50:
    print("Congratulations! You won the game.")

'''
OUTPUT:-

You rolled 2. You gained 2 points. Total points: 2
You rolled 2. You gained 2 points. Total points: 4
You rolled 3. You have to jump!
You rolled 6. You gained 2 points. Total points: 6
You rolled 4. You gained 2 points. Total points: 8
You rolled 4. You gained 2 points. Total points: 10
You rolled 6. You gained 2 points. Total points: 12
You rolled 5. You gained 3 points. Total points: 15
You rolled 1. You have to jump!
Game Over! You rolled a 0.
'''
