# 6-11 try it yourself
cities = {
    'new york city': {
        'country': 'united states',
        'state': 'new york',
        'population': '~8,478,000',
        'fact': 'over 800 languages are spoken in new york city'
    },
        'richmond': {
        'country': 'united states',
        'state': 'virginia',
        'population': '~231,000',
        'fact': 'richmond is named after a town in england'
    },
        'wilmington': {
        'country': 'united states',
        'state': 'delaware',
        'population': '~73,000',
        'fact': 'wilmington is the most populated city in delaware'
    }

}
for city, cityinfo in cities.items():
    country = cityinfo['country']
    state = cityinfo['state']
    population = cityinfo['population']
    fact = cityinfo['fact']
    print(f"\n{city} is in {state}, {country}. the population is {population}, and a fun fact is that {fact}.")
