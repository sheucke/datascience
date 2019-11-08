# FOR LOOPS AND BASIC LIST COMPREHENSIONS

import csv
import requests
nums = range(1, 6)
for num in nums:
    print(num)


# for loop to create a list  of cubes
cubes = []
for num in nums:
    cubes.append(num**3)
print(cubes)

# equivalent list comprehension
cubes = [num ** 3 for num in nums]
print(cubes)

# LIST COMPRENSION WITH CONDITIONS

nums = range(1, 6)

# for loop to create a list of cubes of even numbes

cubes_of_even = []
for num in nums:
    if num % 2 == 0:
        cubes_of_even.append(num**3)

# equivalent list comprehension
cubes_of_even = [num ** 3 for num in nums if num % 2 == 0]
print(cubes_of_even)


# dictionairies

family = {'dad': 'homer', 'mom': 'marge', 'size': 6}

print(family['dad'])
print(len(family))
print(family.keys())
print(family.values())
print(family.items())


with open('2014-average-ticket-price.csv', 'rU') as f:
    data = [row for row in csv.reader(f)]       # list of lists

# examine the data
type(data)
print(len(data))
print(data[0])
print(data[1])

# save the data we want
data = data[1:97]

# step 1: create a list that only contains events
events = [row[0] for row in data]
print(events)

# step 2: create a list tht only contains prices (stored as integer)
prices = [int(row[2]) for row in data]
print(prices)

# step 3: figure out how to locate the away teams
print(events[0])
print(events[0].find('at'))
stop = events[0].find('at')
print(events[0][:stop])

# step 4: use a for loop to make a list of the away teams
away_teams = []
for event in events:
    stop = event.find('at')
    away_teams.append(event[:stop])

print(away_teams)

# step 5: use a for loop to make a list of the home teams
home_teams = []
for event in events:
    start = event.find(' at ') + 4
    stop = event.find(' Tickets ')
    home_teams.append(event[start:stop])
print(home_teams)

# step 6: figure out  how to get prices only for Ravens home games
zip(home_teams, prices)
Raven_home = [price for team, price in zip(
    home_teams, prices) if team == 'Baltimore Ravens']
print(Raven_home)
print(float(sum(Raven_home)) / len(Raven_home))
