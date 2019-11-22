import csv
with open('../data/airline_safety.csv', 'rU') as f:
    data = f.read()

print(data)


with open('../data/airline_safety.csv', 'rU') as f:
    data = f.readlines()

print(data)

# use list comprehension

with open('../data/airline_safety.csv', 'rU') as f:
    data = [row for row in f]

print(data)


with open('../data/airline_safety.csv', 'rU') as f:
    data = [row for row in csv.reader(f)]

print(data)

header = data[0]
data = data[1:]
print(header)

# create a list of airline names (without the star)
# create a list of the same length that contains 1 if there's a star and 0 if not

airlines = []
starred = []
for row in data:
    if row[0][-1] == '*':
        starred.append(1)
        airlines.append(row[0][:-1])
    else:
        starred.append(0)
        airlines.append(row[0])

print(airlines)
print(starred)

# create a list that contains the average number of incidents per distance
print([int(row[2]) + int(row[5]) / float(row[1]) for row in data])

# specify that the delimiter is a tab character
with open('../data/chipotle_orders.tsv', 'rU') as f:
    data = [row for row in csv.reader(f, delimiter='\t')]


'''
PART 2: separate the header and data into two different lists
'''

print(data[0])
print(data[1:])


'''
PART 3: calculate the average price of an order
'''

num_orders = len(set([row[0] for row in data]))
print(num_orders)
print(float(data[1][4][1:-1]))
data = data[1:]
prices = [float(row[4][1:-1]) for row in data]
print(prices)

print(round(sum(prices) / num_orders, 2))

'''
PART 4: create a list of all unique sodas and soft drinks tht they sell
'''

sodas = []
for row in data:
    if 'Canned' in row[2]:
        sodas.append(row[3][1:-1])


unique_sodas = set(sodas)
print(unique_sodas)

'''
PART 5: calculate the average number of toppings per burito
'''

burrito_count = 0
topping_count = 0

# calculate number of toppings by counting the commas and adding 1

for row in data:
    if 'Burrito' in row[2]:
        burrito_count += 1
        topping_count += (row[3].count(',') + 1)

# calculate the average topping count and round to 2 digits
print(round(topping_count / float(burrito_count), 2))


chips = {}

for row in data:
    if 'Chips' in row[2]:
        if row[2] not in chips:
            chips[row[2]] = int(row[1])
        else:
            chips[row[2]] += int(row[1])

print(chips)
