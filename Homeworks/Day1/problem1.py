'''
Problem #1
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
look at the output and find the pattern. Hint - add next letter in the alphabet in each row'''


start = 'a'
end = 'g'
temp = start #creating a temporary variable
while start <= end:
    print(temp)
    start = chr(ord(start) + 1)
    temp=temp+start+temp



'''
OUTPUT:-
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
'''
