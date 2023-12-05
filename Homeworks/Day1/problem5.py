'''
problem #5
In your college Python is taught in 3 different departments by the same professor. 
For each dept, get the no of students studying Python and their marks in the final exam 
Get the input as comma seperated string

Find the top 3 marks in each class
Find the top 3 marks in all classes are combined.
Find the avg mark of students with passing mark in each class and the classes combined.
Find which class has the best average mark and least number of failed students.
'''



import heapq

def is_correct(dep, value, total):
    while len(value) != total:
        print(f"You have entered an incorrect number of marks for dep {dep}.")
        print(f"Please enter {total} marks.")
        value = input(f"Enter the final exam marks of students of dep {dep}:").split(',')
    print(f"You have entered the correct number of marks for dep {dep}.")

def pass_or_fail(marks):
    passmark = 50
    pass_std = []
    fail_std = []
    for mark in marks:
        if int(mark) >= passmark:
            pass_std.append(int(mark))
        else:
            fail_std.append(int(mark))
    return pass_std, fail_std

# getting the total number of students in each department
dep_1_tot = int(input("Enter the no of students in dep 1:"))
dep_2_tot = int(input("Enter the no of students in dep 2:"))
dep_3_tot = int(input("Enter the no of students in dep 3:"))

# getting their marks in the exam for each department
print("Enter the marks separated by commas")
marks_dep_1 = input("Enter the final exam marks of students of dep 1:").split(',')
is_correct(1, marks_dep_1, dep_1_tot)
marks_dep_2 = input("Enter the final exam marks of students of dep 2:").split(',')
is_correct(2, marks_dep_2, dep_2_tot)
marks_dep_3 = input("Enter the final exam marks of students of dep 3:").split(',')
is_correct(3, marks_dep_3, dep_3_tot)
marks_tot = marks_dep_1 + marks_dep_2 + marks_dep_3


# finding the maximum 3 marks without sorting
top_of_dep1 = heapq.nlargest(3, map(int, marks_dep_1))
top_of_dep2 = heapq.nlargest(3, map(int, marks_dep_2))
top_of_dep3 = heapq.nlargest(3, map(int, marks_dep_3))
top_of_all_dep = heapq.nlargest(3, map(int, marks_tot))

# function pass or fail calling
a = pass_or_fail(marks_dep_1)
b = pass_or_fail(marks_dep_2)
c = pass_or_fail(marks_dep_3)
d = pass_or_fail(marks_tot)

# finding the average
avg_1 = sum(a[0]) / len(a[0])
avg_2 = sum(b[0]) / len(b[0])
avg_3 = sum(c[0]) / len(c[0])
tot_avg = sum(d[0]) / len(d[0])

# finding the least number of students
least_1 = len(a[1])
least_2 = len(b[1])
least_3 = len(c[1])
tot_least = len(d[1])

print(f"The top 3 marks in class 1 = {top_of_dep1}")
print(f"The top 3 marks in class 2 = {top_of_dep2}")
print(f"The top 3 marks in class 3 = {top_of_dep3}")
print(f"The top 3 marks in the total class combination = {top_of_all_dep}")
print(f"Average mark in class 1 = {avg_1}")
print(f"Average mark in class 2 = {avg_2}")
print(f"Average mark in class 3 = {avg_3}")
print(f"Average mark in total classes = {tot_avg}")
print(f"Least number of failed students in class 1 = {least_1}")
print(f"Least number of failed students in class 2 = {least_2}")
print(f"Least number of failed students in class 3 = {least_3}")
print(f"Least number of failed students in total class = {tot_least}")



'''
OUTPUT:-
Enter the no of students in dep 1:5
Enter the no of students in dep 2:4
Enter the no of students in dep 3:8
Enter the marks separated by commas
Enter the final exam marks of students of dep 1:45,87,63,87,65,98
You have entered an incorrect number of marks for dep 1.
Please enter 5 marks.
Enter the final exam marks of students of dep 1:45,78,87,96,65
You have entered the correct number of marks for dep 1.
Enter the final exam marks of students of dep 2:86,96,84,23
You have entered the correct number of marks for dep 2.
Enter the final exam marks of students of dep 3:78,63,96,99,54,75,89,41
You have entered the correct number of marks for dep 3.
The top 3 marks in class 1 = [98, 87, 87]
The top 3 marks in class 2 = [96, 86, 84]
The top 3 marks in class 3 = [99, 96, 89]
The top 3 marks in the total class combination = [99, 98, 96]
Average mark in class 1 = 80.0
Average mark in class 2 = 88.66666666666667
Average mark in class 3 = 79.14285714285714
Average mark in total classes = 81.33333333333333
Least number of failed students in class 1 = 1
Least number of failed students in class 2 = 1
Least number of failed students in class 3 = 1
Least number of failed students in total class = 3
'''
