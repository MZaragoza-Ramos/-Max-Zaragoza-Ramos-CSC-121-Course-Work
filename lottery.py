#Function that hold the lottery ticket code
def lottery():
    from random import randint
    from random import choice

    """Creates a winning lottery ticket and checks to 
    see if the inputed ticket matches
    """
    lucky_numbers = randint(1000, 9999)

    vowels = ['a', 'e', 'i', 'o', 'u']
    lucky_vowel = choice(vowels)

    winning_ticket = f"{lucky_numbers}{lucky_vowel}"

    prompt = "Please enter your lottery number to see if you won!"
    prompt += "\n(All tickets are four numbers long with a vowel at the end): "
    ticket = input(prompt)

    if ticket == winning_ticket:
        print("\nCongratulations, you have won the lottery!")
    else:
        print("\nSorry, you did not win today. Better luck next time!")

lottery()