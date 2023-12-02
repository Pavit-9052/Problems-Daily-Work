'''
Problem #3
Write a program that calculates the profit generated by a movie theatre for different ticket classes.

For VIP tickets, the profit is 30% of the ticket price + Rs120 for every ticket sold.
For General tickets, the profit is 20% of the ticket price + Rs80 for every ticket sold.
For Matinee show tickets, the profit is a flat 15% of the ticket price.
Input: Ticket price and number of tickets sold for each ticket class.
Output: Calculate and print the total revenue generated by the theatre in a day.


Same as above. But, from profit, entertainmant tax need to be subtracted. 
Tax is 5% of the cost of the ticket.
'''


def calculate_revenue_with_tax(ticket_class, price, tickets_sold):
    if ticket_class == "VIP":
        revenue = 0.30 * price + 120 * tickets_sold
    elif ticket_class == "General":
        revenue = 0.20 * price + 80 * tickets_sold
    elif ticket_class == "Matinee":
        revenue = 0.15 * price
    else:
        print("Invalid ticket class")
        return None
    
   
    revenue -= 0.05 * revenue
    
    return revenue

def main():
    total_revenue = 0

    # VIP Tickets
    price_vip = float(input("Enter VIP ticket price: "))
    tickets_sold_vip = int(input("Enter number of VIP tickets sold: "))
    total_revenue += calculate_revenue_with_tax("VIP", price_vip, tickets_sold_vip)

    # General Tickets
    price_general = float(input("Enter General ticket price: "))
    tickets_sold_general = int(input("Enter number of General tickets sold: "))
    total_revenue += calculate_revenue_with_tax("General", price_general, tickets_sold_general)

    # Matinee Tickets
    price_matinee = float(input("Enter Matinee ticket price: "))
    tickets_sold_matinee = int(input("Enter number of Matinee tickets sold: "))
    total_revenue += calculate_revenue_with_tax("Matinee", price_matinee, tickets_sold_matinee)

    print(f"Total revenue generated by the theatre (after tax): Rs{total_revenue:.2f}")


main()


'''
OUTPUT:-
Enter VIP ticket price: 500
Enter number of VIP tickets sold: 5
Enter General ticket price: 750
Enter number of General tickets sold: 3
Enter Matinee ticket price: 69
Enter number of Matinee tickets sold: 4
Total revenue generated by the theatre (after tax): Rs1092.83
'''
