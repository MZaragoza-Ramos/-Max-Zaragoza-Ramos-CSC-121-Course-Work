print("Please type in two number to add them together!")
print("Type 'q' at any point to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Oops, it seems like an input was not a number, try again.")
    else:
        print(answer)