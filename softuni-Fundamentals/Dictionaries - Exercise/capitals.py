def capitals():
    countries = input().split(", ")
    capital = input().split(", ")
    result = dict(zip(countries, capital))

    for countries, capital in result.items():
        print(f"{countries} -> {capital}")


capitals()
