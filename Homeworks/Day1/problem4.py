'''
Problem #4
write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda (a is moved to the right)
abcd is same as cdab 
abcd is  not same as cdba

123456 = 456123
123456 not = 412356
hint - 
there are many simple answers. you can try with slice function
'''


def is_same(str1, str2):
    if (len(str1) != len(str2)):
        return False
    temp = str1 + str1
    return (str2 in temp)

str1 = "ABCD"
str2 = "CDAB"
if (is_same(str1, str2)):
    print("Strings are same")
else:
    print("Strings are not same")


'''
OUTPUT:-
Strings are same
'''
