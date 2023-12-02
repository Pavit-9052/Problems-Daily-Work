'''
In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
'''


def find_between_letters(sentence, letter):
    output = ''
    first_letter_index = sentence.find(letter)
    last_letter_index = sentence.rfind(letter)

    if first_letter_index != -1 and last_letter_index != -1 :
        for i in range(first_letter_index + 1, last_letter_index):
            output += sentence[i]
        print(output)
    else:
        print(f"No {letter} found or only one {letter} found.")

def find_between_a_b(sentence):
    find_between_letters(sentence, 'a')
    find_between_letters(sentence, 'b')

sentence = input("Enter a sentence: ")
find_between_a_b(sentence)



'''
OUTPUT:-

Enter a sentence: abcdefghbakealkb
bcdefghbake
cdefghbakealk

'''
