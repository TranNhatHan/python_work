def format_location(city, country, population=0):
    if population:
        return f"{city.title()}, {country.title()} - {population}"
    else:
        return f"{city.title()}, {country.title()}"