#Function that holds a dictionary containing the dream car's information
def dream_car(manufacturer, model, **car_info):
    """Creates a dictionary containing details of a dream car."""
    car_info['car manufacturer'] = manufacturer.title()
    car_info['car model'] = model.title()
    return car_info

#Gets the arguements for the function and prints out the result
car_info = dream_car('ford', 'mustang', year=2025, price=('$66,673'))
print(car_info)