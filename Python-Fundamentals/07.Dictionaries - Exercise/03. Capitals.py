country = input().split(", ")
capitals = input().split(", ")
information = {country[index]: capitals[index] for index in range(len(country))}

for country, capitals in information.items():
    print(f"{country} -> {capitals}")
