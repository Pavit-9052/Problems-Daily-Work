'''
Problem #2
Read a passage from a file. 
Count the number of times the word 'the' followed by another 'the' without 'a' in between.
Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.
answer is 4 (The king, the forest, The King the next).
Make sure your code includes exception handling for reading from a file.
'''


def count_the(passage):
    words = passage.split()
    count = 0
    for i in range(len(words) - 1):
        if words[i].lower() == 'the' and words[i + 1].lower() == 'the' and 'a' not in words[i:i+2]:
            count += 1
    return count
# Example 
passage = "The king went to the forest with the wife and a servant. The king shot a deer. The king went to the forest again the next day."
result = count_the(passage)
print(f"The number of occurrences of 'the the' without 'a' in between is: {result}")


'''
OUTPUT:-
The number of occurrences of 'the the' without 'a' in between is: 0
'''
