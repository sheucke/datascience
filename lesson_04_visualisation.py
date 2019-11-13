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
pd.plotting.scatter_matrix(drinks)
plt.show()

drinks.groupby(
    'continent').total_litres_of_pure_alcohol.mean().plot(kind='bar')
plt.show()

# homework

auto = pd.read_table('../data/auto_mpg.txt', sep='|')

auto.groupby('cylinders').mpg.mean().plot(kind='bar')
plt.title("Comparing Mean MPG for Different Numbers of Cylinders")
plt.xlabel("Number of Cylinders")
plt.ylabel("Average MPG")
plt.show()

pd.plotting.scatter_matrix(auto)


pd.plotting.scatter_matrix(auto, c=auto.mpg)
plt.show()

# do heavier of ligther cars get better mpg
auto.plot(kind='scatter', x='weight', y='mpg', alpha=0.5)
plt.title('Car MPG by Weight')
plt.xlabel('Car weight')
plt.ylabel('MPG')
plt.show()

auto.plot(kind='scatter', x='displacement', y='horsepower', alpha=0.5)
plt.title('Horsepower by Engine Displacement')
plt.xlabel('Engine Displacement')
plt.ylabel('Horsepower')
plt.show()
