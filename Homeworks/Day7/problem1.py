'''
Problem 1
In the input, find the first A and last A, print all the letters between these two A.
'''


def find_between_a(sentence):
    output = ''
    first_a_index = sentence.find('a')
    last_a_index = sentence.rfind('a')
    for i in range(first_a_index + 1, last_a_index):
        output += sentence[i]
    print(output)

sentence = input("Enter a sentence: ")
find_between_a(sentence)


'''
OUTPUT:-
Enter a sentence: Pavithraboea
vithraboe
'''
