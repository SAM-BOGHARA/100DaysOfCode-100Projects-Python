# nesting dictionary in a dictionary

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 34}
# }

# print(travel_log["Germany"])
travelling = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
     },
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 34
     }
]


def add_new_country(country_visited, cities_visited, times_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = times_visited
    travelling.append(new_country)


add_new_country(country_visited="Russia", cities_visited=["Moscow", "Saint P", "alexa"], times_visited = 2)

print(travelling)
