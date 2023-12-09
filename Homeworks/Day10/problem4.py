'''
Problem #4
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output =  15
explanation (1 + 2) * 5 = 15

input ["10", "2", "3", "+","-", "5", "*"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
Hint : Use the concept of stack. Push and pop. 
Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
operator, pop two elements from the stack, apply the operation and push the result back.
'''


def calculate(expression):
    stack = []
    operators = ['+', '-', '*', '/']

    for item in expression:
        if item not in operators:
            stack.append(int(item))
        else:
            operand_2 = stack.pop()
            operand_1 = stack.pop()

            if item == '+':
                result = operand_1 + operand_2
            elif item == '/':
                result = operand_1 / operand_2
            elif item == '-':
                result = operand_1 - operand_2
            else:
                result = operand_1 * operand_2

            stack.append(result)

    return stack[0]


expression1 = ["1", "2", "+", "5", "*"]
result1 = calculate(expression1)
print("Input 1:",expression1)
print("Output:",result1) 

expression2 = ["10", "2", "3", "+","-", "5", "*"]
result2 = calculate(expression2)
print("Input 2:",expression2)
print("Output:",result2) 


'''
OUTPUT:-
Input 1: ['1', '2', '+', '5', '*']
Output: 15
Input 2: ['10', '2', '3', '+', '-', '5', '*']
Output: 25
'''
