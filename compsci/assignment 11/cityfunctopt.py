def city_country(city, country, population=0):
    output = f"{city()}, {country()}"
    if population:
        output += f" population = {population}"
    return output