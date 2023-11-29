'''
Problem #1
Print the following pattern
1
212
32123
4321234
543212345
Get user input for how far to go (up to 0)
'''


a = 1
n = int(input("Enter the number: "))
print(a)
for i in range(1, n): #To print the pattern
    a = a + 1
    for j in range(a, 0, -1):#To print in reverse order
        print(j, end="")
    
    for j in range(2, a + 1):#To print in correct order
        print(j, end="")
    print()#To move to the next line



'''
OUTPUT:-
Enter the number: 6
1
212
32123
4321234
543212345
65432123456
'''
