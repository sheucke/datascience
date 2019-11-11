"""
Pandas for Data Exploration, Analysis, and Visualization
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

drinks = pd.read_table('../data/drinks.csv', sep=',')
print(drinks.head())
print(drinks.tail())
print(drinks.describe())
print(drinks.describe(include='all'))
print(drinks.index)
print(drinks.columns)
print(drinks.dtypes)
print(drinks.shape)
print(drinks.values)
print(drinks.info())

# print the 'beer_servings' Series (a single column)
drinks.beer_servings
drinks['beer_servings']
type(drinks.beer_servings)

# print two columns
drinks[['beer_servings', 'wine_servings']]
cols = ['beer_servings', 'wine_servings']
drinks[cols]

# Calculate the average 'beer_servings' for the entire dataset
print(drinks.describe())
print(drinks.beer_servings.describe())
print(drinks.beer_servings.mean())
print(drinks.beer_servings.max())
print(drinks.beer_servings.min())

# other aggregation functions
print(drinks.beer_servings.sum())
print(drinks.beer_servings.count())
print(float(drinks.beer_servings.sum() / drinks.beer_servings.count()))

print(drinks.continent.value_counts())

# Simple logical filters

print(drinks.continent == 'EU')
print(drinks[drinks['continent'] == 'EU'])
print(drinks[drinks.continent == 'EU'])

print(drinks[drinks.beer_servings > 158])
print(drinks[drinks.beer_servings <= 10])
print(drinks[drinks.beer_servings <= 10][['country', 'beer_servings']])

# Calculate the average 'beer_servings' for all of Europe
print(drinks[drinks.continent == 'EU'].beer_servings.mean())

print(drinks[(drinks.continent == 'EU') & (drinks.wine_servings > 300)])


print(drinks[(drinks.continent == 'EU') | (drinks.wine_servings > 300)])

print(drinks.sort_index(by='total_litres_of_pure_alcohol').tail(10))
