'''
Problem #3
Its is a single player game where the user starts with 0 points. User keeps rolling the 
dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
 added. If the number is odd, then if the number is 1,3 then the user has to jump. 
 If the number is 5, then 3 points are added. The game ends when the user has 50 points.
 '''

import random

def dice_roll():
    return random.randint(1, 6)
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

You rolled 5. You gained 3 points. Total points: 3
You rolled 2. You gained 2 points. Total points: 5
You rolled 2. You gained 2 points. Total points: 7
You rolled 2. You gained 2 points. Total points: 9
You rolled 2. You gained 2 points. Total points: 11
You rolled 6. You gained 2 points. Total points: 13
You rolled 1. You have to jump!
You rolled 5. You gained 3 points. Total points: 16
You rolled 5. You gained 3 points. Total points: 19
You rolled 3. You have to jump!
You rolled 6. You gained 2 points. Total points: 21
You rolled 5. You gained 3 points. Total points: 24
You rolled 1. You have to jump!
You rolled 6. You gained 2 points. Total points: 26
You rolled 6. You gained 2 points. Total points: 28
You rolled 5. You gained 3 points. Total points: 31
You rolled 2. You gained 2 points. Total points: 33
You rolled 4. You gained 2 points. Total points: 35
You rolled 4. You gained 2 points. Total points: 37
You rolled 1. You have to jump!
You rolled 6. You gained 2 points. Total points: 39
You rolled 6. You gained 2 points. Total points: 41
You rolled 6. You gained 2 points. Total points: 43
You rolled 3. You have to jump!
You rolled 1. You have to jump!
You rolled 2. You gained 2 points. Total points: 45
You rolled 2. You gained 2 points. Total points: 47
You rolled 3. You have to jump!
You rolled 6. You gained 2 points. Total points: 49
You rolled 3. You have to jump!
You rolled 2. You gained 2 points. Total points: 51
Congratulations! You won the game.
'''
