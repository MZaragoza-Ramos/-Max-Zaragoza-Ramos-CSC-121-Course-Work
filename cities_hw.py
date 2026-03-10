#Function used to print out a city in a country 
# with its default value being set to 'cuba'
def describe_city(city, country='cuba'):
    """Display a city from a country"""
    print(f"\n{city.title()} is a city in {country.title()}.")
#Two calls for the function with a correct city
describe_city('havana')
describe_city('nueva gerona')
#A call for the gunction with an incorrect city
describe_city('chicago')