'''
Problem #1
write a program that reads a passage and reverses the order of 
letters in each word while keeping the word order intact. Use function.
Eg- input - I am Sayur
Output I ma ruyaS
'''

def reverse(sentence):
    words = sentence.split()
    for word in words:
        print(word[::-1],end=" ")  #print the words in reverse order
sentence = input("Enter a sentence:")
reverse(sentence)
        

'''
OUTPUT:-
Enter a sentence:I am Sayur
I ma ruyaS
'''
