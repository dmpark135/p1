cities = {
        'seoul':{'country':'korea',
                 'population':'50m',
                 'one fact': 'hot chicks'},
         'london':{'country':'UK',
                   'population':'30m',
                   'one fact':'likes fish n chips'},
            }
for city, facts in cities.items():
    print(f'\nCities: {city.title()}')
    x = facts['country'] 
    s= facts['one fact']
    country = x+" "+s
    population = facts['population']
    one_fact = facts['one fact']
    
    print(f'\tCountry: {country.title()}' )
    print(f'\tPopulation: {population.title()}')
    print(f'\tOne Fact: {one_fact.title()}')
    