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
