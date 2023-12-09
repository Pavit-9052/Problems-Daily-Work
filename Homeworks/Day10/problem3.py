'''
Problem #3 
Add two number represented in a list as reversed. print the sum also as a list in reverse order
eg input list1 = [1,2,3] list2 = [5,6,7]
answer= [6,8,0,1]
 explanation (321 + 765 = 1086)
'''



list1 = [1, 2, 3]
list2 = [5, 6, 7]

lis1_reverse=int(''.join(map(str, list1[::-1])))#To sort it in reverse then join them as a number
list2_reverse=int(''.join(map(str, list2[::-1]))) 

output =lis1_reverse+list2_reverse #Adding after reversing both numbers

output_reverse = list(map(int, str(output)[::-1])) #Converting the output as list after reversing it
print("The output:",output_reverse)


'''
OUTPUT:-
The output: [6, 8, 0, 1]
'''


