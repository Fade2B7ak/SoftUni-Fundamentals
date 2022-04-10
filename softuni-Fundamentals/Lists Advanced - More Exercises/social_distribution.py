population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())

for index in range(len(population)):
    if population[index] < minimum_wealth:
        needed = minimum_wealth - population[index]
        wealthiest = max(population)
        if wealthiest - needed >= minimum_wealth:
            population[population.index(wealthiest)] -= needed
            population[index] += needed
if sum(population) >= len(population) * minimum_wealth:
    print(population)
else:
    print("No equal distribution possible")