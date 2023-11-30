'''
Problem #1
write a program that reads a passage and reverses the order of 
letters in each word while keeping the word order intact. Use function.
Eg- input - I am Sayur
Output I ma ruyaS
'''

def reverse(sentence):
    words = sentence.split()
    reversed_words = []

    for i in words:
        reversed_word = i[::-1]
        reversed_words.append(reversed_word)

    reversed_passage = ' '.join(reversed_words)
    return reversed_passage
input_sen = "I am Sayur"
output_sen = reverse(input_sen)

print(f"Input:  {input_sen}")
print(f"Output: {output_sen}")



'''
OUTPUT:-
Input:  I am Sayur
Output: I ma ruyaS
'''
