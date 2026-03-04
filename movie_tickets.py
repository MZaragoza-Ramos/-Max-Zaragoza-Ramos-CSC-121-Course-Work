#A prompt for the customer to read
prompt = ("Hello, and welcome to the movie theater!")
prompt += ("\nEnter your age to see how much your ticket cost: ")
#Allows the customers to type in their ages and converts ages into intergers
message = input(prompt)
customer_age = int(message)
#Customers are given a ticket price based on their age
if customer_age < 3:
        price = 0
        print("Your ticket is free.")
elif customer_age >= 3 and customer_age <= 12:
        price = 10
        print(f"Your ticket costs ${price}.")
else:
        price = 15
        print(f"Your ticket is ${price}.")
#A new prompt asking for how many tickets they want
prompt = ("How many tickets would you like? ")
#Allows the customers to type in the amount of tickets they want
message = input(prompt)
tickets = int(message)
#Gives the total cost of the tickets
total_cost = price * tickets
print(f"Your total ticket cost is ${total_cost}")