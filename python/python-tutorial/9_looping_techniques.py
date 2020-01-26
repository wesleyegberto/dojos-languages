# Looping techniques

# === Lists ===

# loop a sequence getting the index
for index, hero in enumerate(['hulk', 'wolverine', 'professor x']):
    print(index, hero)

# loop over two sequences
countries = ['Brazil', 'France', 'USA']
cities = ['Sao Paulo', 'Paris', 'New York']
for country, city in zip(countries, cities):
    print('{1} is in {0}'.format(country, city))

# loop over a sequence in reverse
for i in reversed(range(1, 10, 2)):
    print(i)
