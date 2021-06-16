# Loop

cities = ["new york city","yangon","tokyo","seoul"]

for city in cities:
    print(city.title())

capatialized_cities = []

for city in cities:
    capatialized_cities.append(city.title())

print(capatialized_cities)

# Range(start,end,step)

print(list(range(0,3)))
print(list(range(4,8)))
print(list(range(1,20,4)))

for number in range(4):
    print(number)

for index in range(len(cities)):
    cities[index] = cities[index].title()

print(cities)
