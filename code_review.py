#Code review of the magicians example program
#List of magicians
magicians = ['alice', 'david',
             'carolina'
]
#For loop that prints a repeated message for each magicians
for magician in magicians:
        print(f"{magician.title()}, that was a great trick!")
        print(f"I can't wait to see your next trick, {magician.title()}.\n")
#A message printed out for all magicians
print("Thank you, everyone. That was a great magic show!")

#A code review of the foods example program
#List of my favorite foods
my_foods = ['pizza', 'falafel',
            'carrot cake'
]
#Copying my food list to my friend's food list
friend_foods = my_foods[:]
#Appending new foods to it
my_foods.append('cannoli')
friend_foods.append('ice cream')
#Two statements are printed out showing the content of the lists
print("\nMy favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#Code review of the animals program
#List of animals
animals = ['meerkat', 'red panda',
           'raccoon'
]
#A For loop for the animals
for animal in animals:
        print(f"\nA {animal} has a dark circle of fur around its eyes.")
print("\nAll these animals have a dark circle of fur around their eyes.")