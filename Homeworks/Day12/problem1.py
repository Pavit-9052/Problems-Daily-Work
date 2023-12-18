'''
Problem #1
You have list of unique words. you input is a string with no spaces. Return true if the letters in the 
input string can be seperated into words that are in the list.
eg list = ["we", "students", "are" ]
input = "wearestudents"
output = true
eg 2 List = ["we", "doctor","and", "nurse", "are"]
input = "wearenurseandoctor"
output = False 
input = "wearenurseanddoctor"
output = true
'''


def is_same(list_input):
    dictionary={}
    for item in list_input:  
        if item in dictionary:  #If value present in dictionary increase count
            dictionary[item]+=1
        else:                  #If not include it in dictionary
            dictionary[item]=1
    return dictionary
        
        
input1=input("Enter the words separated by spaces:").split()
input_list=''.join(input1)

sentence=input("Enter the sentence:")

dict1=is_same(input_list)
dict2=is_same(sentence)

#To sort the dictionary for checking for equal characters
sorted_dict1 = dict(sorted(dict1.items()))  
sorted_dict2 = dict(sorted(dict2.items()))

print(sorted_dict1)
print(sorted_dict2)

result= sorted_dict1==sorted_dict2
print("The output:",result)

'''
OUTPUT:-

Enter the words separated by spaces:we are doctor and nurse
Enter the sentence:weandoctornurseare
{'a': 2, 'c': 1, 'd': 2, 'e': 3, 'n': 2, 'o': 2, 'r': 3, 's': 1, 't': 1, 'u': 1, 'w': 1}
{'a': 2, 'c': 1, 'd': 1, 'e': 3, 'n': 2, 'o': 2, 'r': 3, 's': 1, 't': 1, 'u': 1, 'w': 1}
The output: False


Enter the words separated by spaces:we doctor and nurse are
Enter the sentence:wenurseanddoctorare
{'a': 2, 'c': 1, 'd': 2, 'e': 3, 'n': 2, 'o': 2, 'r': 3, 's': 1, 't': 1, 'u': 1, 'w': 1}
{'a': 2, 'c': 1, 'd': 2, 'e': 3, 'n': 2, 'o': 2, 'r': 3, 's': 1, 't': 1, 'u': 1, 'w': 1}
The output: True

'''
