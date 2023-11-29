'''
Problem #2
you have a list of student names and another list with their marks in CS. 
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.
'''


names=["Pavithra","Abisha","Sanjana","Karthic Selvi","Abirami","DhanuSri","Sangetha","Madhu","Anu","Vidhya","Vishaka"]
marks=[80,53,12,45,32,96,78,23,56,26,3]
count=0
print("Passed students:-")
for i,j in zip(names,marks):  #zip to iterate over two list at a time
    if j < 50:
        count+=1
    else:
        print("Name:",i," Mark :",j)
print("No of failed students :",count)



'''
Output:-
Passed students:-
Name: Pavithra  Mark : 80
Name: Abisha  Mark : 53
Name: DhanuSri  Mark : 96
Name: Sangetha  Mark : 78
Name: Anu  Mark : 56
No of failed students : 6
'''
