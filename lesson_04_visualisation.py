import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

drinks = pd.read_csv('../data/drinks.csv')

# bar plot of number of countries in each continent
drinks.continent.value_counts().plot(kind='bar', title='Countries per Continent')
plt.xlabel('Continent')
plt.ylabel('Count')
plt.show()

# bar plot of average number of beer servings by continent
drinks.groupby('continent').beer_servings.mean().plot(
    kind='bar', title='Average Number of Beer Servings By Continent')
plt.ylabel('Average Number of Beer Servings Per Year')
plt.show()

# histogram of beer servings
drinks.beer_servings.hist(bins=20)
plt.title('Distribution of Beer Servings')
plt.xlabel('Beer Servings')
plt.ylabel('Frequency')
plt.show()


# density plot of beer servings (smooth version of a histogram)
drinks.beer_servings.plot(kind='density', xlim=(0, 500))
plt.title('Distribution of Beer Servings')
plt.xlabel('Beer Servings')
plt.show()

# grouped histogram of beer servings (shows the distribution for each group)
drinks.beer_servings.hist(by=drinks.continent)
plt.show()

drinks.beer_servings.hist(by=drinks.continent, sharex=True)
plt.show()

drinks.beer_servings.hist(by=drinks.continent, sharex=True, sharey=True)
plt.show()

# change layout (new in pandas 0.15.0)
drinks.beer_servings.hist(by=drinks.continent, sharey=True, layout=(2, 3))
plt.show()

# boxplot of beer servings by continent
drinks.boxplot(column='beer_servings', by='continent')
plt.show()

# scatterplot of beer servings versus wine servings
drinks.plot(kind='scatter', x='beer_servings', y='wine_servings', alpha=0.3)
plt.show()

drinks.plot(kind='scatter', x='beer_servings', y='wine_servings',
            c='spirit_servings', colormap='Blues')
plt.show()

colors = np.where(drinks.continent == 'EU', 'r', 'b')
drinks.plot(x='beer_servings', y='wine_servings', kind='scatter', c=colors)
plt.show()

# Scatter matrix
pd.scatter_matrix(drinks)
plt.show()
