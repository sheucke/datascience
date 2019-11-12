import pandas as pd

# read text file and use '|' as separator
auto = pd.read_table('../data/auto_mpg.txt', sep='|')

print(auto.shape)
print(auto.columns)
print(auto.info())

print(auto.describe())
print(auto.min(numeric_only=True))
print(auto.max(numeric_only=True))

# range
print(auto.max(numeric_only=True) - auto.min(numeric_only=True))

print(auto.mean())
print(auto.median())

print(auto.mean() - auto.median())

# 5 cars that get best gas mileage
print(auto.sort_index(by='mpg', ascending=False)[0:5][['car_name', 'mpg']])

# 5 cars with more than 4 cylinders that get the best gas mileage
print(auto[auto.cylinders > 4].sort_index(
    by='mpg', ascending=False)[0:5][['car_name', 'mpg']])

# 5 cars that get best gas mileage
print(auto.sort_index(by='mpg')[0:5][['car_name', 'mpg']])

print(auto[auto.cylinders > 4].sort_index(
    by='mpg')[0:5][['car_name', 'mpg']])

print(auto.groupby(by='cylinders').mpg.mean())
print(auto.groupby(by='model_year').mpg.mean())

print(auto[auto.weight <= auto.weight.median()].mpg.mean())
print(auto[auto.weight > auto.weight.median()].mpg.mean())
