'''
Problem #3
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.
'''



names=["Pavithra","Abisha","Sanjana","Karthic Selvi","Abirami","DhanuSri"]
cs_marks=[78,99,56,88,60,40]
math_marks=[32,98,45,89,70,86]
eng_marks=[65,99,76,81,74,3]
for n,cs,mat,eng in zip(names,cs_marks,math_marks,eng_marks):
  if ((cs>=90 and mat>=90 and eng>=90)or cs>=80 or mat>=80 or eng>=80):
    print(n)


'''
OUTPUT:-
Abisha
Karthic Selvi
DhanuSri
'''
