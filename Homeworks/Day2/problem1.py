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


start = '1'
temp = 1  
while temp <= 9:   #print upto 9
    print(start)
    start = str(temp+1) + start + str(temp+1)  #temp=1 so str(temp+1) ='2' then concatenating it with start and '2' gives 212
    temp += 1


'''
OUTPUT:-
1
212
32123
4321234
543212345
65432123456
7654321234567
876543212345678
98765432123456789
'''
