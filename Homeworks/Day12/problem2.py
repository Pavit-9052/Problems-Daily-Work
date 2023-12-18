'''
Problem #2
Input is an integer list and another integer k. Output is the k most frequently occuring numbers.
output can be in any order.
eg input = [1,1,1,2,2,3,5,5,5,5], k =2
output [1,5] (top 2 most frequently occuring numbers)
input = [4,5,4,5,4,5,3,3,3,7,8,1,1,1], k = 4
output [4,5,3,1]
'''


list_input=input("Enter the numbers separated by space:").split()
key=int(input("Enter the key value:"))
dictionary={}
output=[]
for item in list_input:  
    if item in dictionary:  #If value present in dictionary increase count
        dictionary[item]+=1
    else:                  #If not include it in dictionary
        dictionary[item]=1
for k in dictionary:       #Iterating over dictionary
    if dictionary[k]>= key: #Check if value is graeter than or equal to key
        output.append(k)
print("The output is:",output)



'''
OUTPUT:-
Enter the numbers separated by space:1 1 1 1 2 3 5 7 8 9 6 6 6 8 7 9 9 2
Enter the key value:3
The output is: ['1', '9', '6']
'''
