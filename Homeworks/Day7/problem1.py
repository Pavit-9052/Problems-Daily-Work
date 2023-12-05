'''
Problem 1
In the input, find the first A and last A, print all the letters between these two A.
'''


def find_between_a(sentence):
    output = ''
    first_a_index = sentence.find('a')    #finds 1st a
    last_a_index = sentence.rfind('a')    #finds last a
    for i in range(first_a_index + 1, last_a_index):   #no need to print 1st index which is 'a' so (1st index+1 to last index) which is automatically last index-1
        output += sentence[i]
    print(output)

sentence = input("Enter a sentence: ")
find_between_a(sentence)


'''
OUTPUT:-
Enter a sentence: Pavithraboea
vithraboe
'''
