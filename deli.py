#List of sandwich orders at the del
sandwich_orders = ['american sub', 'bacon, egg, and cheese sandwich', 
                    'barbecue sandwich', 'philly cheesesteak',                    
]
#Empty list of finished orders
finished_sandwiches = []
#The while loops goes through all the sandwich orders, prints a message, and
#puts them in the finished sandwich list
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"The {current_sandwich.title()} is done!")
    finished_sandwiches.append(current_sandwich)
#When all the sandwich orders are done, a message is printed out
print("\nThese are all the sandwiches that were made today:")
for sandwich in finished_sandwiches:
    print(sandwich.title())