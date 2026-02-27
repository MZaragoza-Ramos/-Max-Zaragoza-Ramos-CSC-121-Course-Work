#Dictionary of favorite places with the values being a list
favorite_places = {
    'max': ['mexico', 'north carolina'],
    'jessica': ['tokyo', 'iceland'],
    'allison': ['singapore', 'new zealand'],
}
#A for loop to print out each person's favorite place
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for place in places:
        print(place.title())