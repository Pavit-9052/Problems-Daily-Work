'''
You have a list of numbers in ascending order, but with duplicates.
Remove the duplicated, append _ at the end for each duplicate removed 
eg input = [1,2,3,3,3,4,4,7,7,9]
output = [1,2,3,4,7,9,_,_,_,_]

Problem #2
Same as above,but print the list in descending order
input = [1,2,3,3,3,4,4,7,7,9]
output = [9,7,4,3,2,1,_,_,_,_]
'''


input = [1,2,3,3,3,4,4,7,7,9]
output=[]
count_duplicate=0
for i in input: 
    if i not in output:  #Check if number is in output
        output.append(i)
    else:
        count_duplicate+=1  #If not in output then increase count to find total no of duplicates 
output.sort(reverse=True) #To print in descending order
while count_duplicate!=0: #To print the underscores
    output.append("_")
    count_duplicate-=1

print("The input:",input)
print("The output:",output)



'''
OUTPUT:-
The input: [1, 2, 3, 3, 3, 4, 4, 7, 7, 9]
The output: [9, 7, 4, 3, 2, 1, '_', '_', '_', '_']
'''

