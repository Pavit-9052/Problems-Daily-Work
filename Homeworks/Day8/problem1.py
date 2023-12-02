'''
Identify which portion of the code can be written as a function in all the programs below

Problem #1.
Write a program for calculating the profit for railways.
For first class tickets, the profit is 25% of the price + Rs100 for every ticket sold.
For Second class tickets, the profit is 15% of the price + Rs70 for every ticket sold.
For Third class tickets (i don't know if there is a third class), the profit is 5% of the price.

Get the price and no of tickets sold for each class and calculate the total profit. 
Identity what calculation in the above problem can be written as a function 
and what the input and output should be.
'''
def calculate_profit(ticket_class, price, tickets_sold):
    if ticket_class == "1":
        profit = 0.25 * price + 100 * tickets_sold
    elif ticket_class == "2":
        profit = 0.15 * price + 70 * tickets_sold
    elif ticket_class == "3":
        profit = 0.05 * price
    else:
        print("Invalid ticket class")
        return None
    
    return profit

ticket_class = input("Enter ticket class (1/2/3): ")
price = float(input("Enter ticket price: "))
tickets_sold = int(input("Enter number of tickets sold: "))

total_profit = calculate_profit(ticket_class, price, tickets_sold)

if total_profit is not None:
    print(f"Total profit for class {ticket_class}: Rs{total_profit:.2f}")



'''
OUTPUT:-
Enter ticket class (1/2/3): 3
Enter ticket price: 500
Enter number of tickets sold: 5
Total profit for class 3: Rs25.00
'''
