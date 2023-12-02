'''
Problem 3:
  In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B after the first A (if there is a A) and last B and print all the letters between these two B. 
  
  If there is no B or 2nd B is not found, find the first C after the first B (if there is a B) and last C and print all the letters between these two C. 
'''
def find_between_A_B_C(sentence):
    output = ''
    sentence = sentence.lower()
    first_A_index = sentence.find('a')
    last_A_index = sentence.rfind('a')
    if first_A_index == -1 or first_A_index == last_A_index:
        if first_A_index != -1:
            first_B_index = sentence.find('b', first_A_index)
            last_B_index = sentence.rfind('b')
            if first_B_index == -1 or first_B_index == last_B_index:
                if first_B_index != -1:
                    first_C_index = sentence.find('c', first_B_index)
                    last_C_index = sentence.rfind('c')
                    if first_C_index == -1 or first_C_index == last_C_index:
                        print("No occurrences of B or C found after the first A.")
                    else:
                        output = sentence[first_C_index + 1:last_C_index]
                        print(output)
                else:
                    print("No occurrences of B found after the first A.")
            else:
                output = sentence[first_B_index + 1:last_B_index]
                print(output)
        else:
            print("No occurrences of A found in the sentence.")
    else:
        output = sentence[first_A_index + 1:last_A_index]
        print(output)
sentence = input("Enter a sentence: ")
find_between_A_B_C(sentence)


'''
OUTPUT:-
Enter a sentence: abishekBnubk
ishekbnu
'''
