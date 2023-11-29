'''
Problem #2
Write a program that reads a passage or string and counts the occurrences of two consecutive words 
that are the same without any other specific word in between.
 For example, count the occurrences of "apple apple" but not "apple orange apple."
 '''

sentence = 'pavi abi pavi pavi abi abi abi pavi a a'
words = sentence.split()
dict1 = {}

for i in range(len(words) - 1):
    if words[i] == words[i + 1]:
        repeat_word = words[i]
        if repeat_word in dict1:
            dict1[repeat_word] += 1
        else:
            dict1[repeat_word] = 1

print("Occurrences of words:")
for word, count in dict1.items():
    print(f"{word}: {count}")


'''
OUTPUT:-
Occurrences of words:
pavi: 1
abi: 2
a: 1
'''
