#Dictionary of rivers and their respective countries
rivers = {'nile': 'egypt', 
          'amazon river': 'brazil',
          'rio grande': 'mexico',
          'huanghe': 'china'
          }
#A for loop that prints which rivers flows through which country
for river, country in rivers.items():
        print(f"The {river.title()} flows through {country.title()}.")
#A for loop printing each river in the dictionary
for river in rivers.keys():
        print(f"\n{river.title()}")
#A for loop printing each country in the dictionary
for country in rivers.values():
        print(f"\n{country.title()}")