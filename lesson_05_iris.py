
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the iris data into a pandas DataFrame, including column names
col_names = ['sepal_length', 'sepal_width',
             'petal_length', 'petal_width', 'species']
iris = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                   names=col_names)

# gather basic information
print(iris.shape)
print(iris.head())
print(iris.describe())
print(iris.species.value_counts())
print(iris.dtypes)
print(iris.isnull().sum())

# use groupby to look for differences between the species
print(iris.groupby('species').sepal_length.mean())
print(iris.groupby('species').mean())
print(iris.groupby('species').describe())

# use sorting to look for differences between the species
print(iris.sort_index(by='sepal_length').values)


# use plotting to look for differences between the species
iris.petal_width.hist(by=iris.species, sharex=True)
iris.boxplot(column='petal_width', by='species')
iris.boxplot(by='species')

iris['species_num'] = iris.species.map(
    {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})
iris.plot(kind='scatter', x='petal_length', y='petal_width',
          c='species_num', colormap='Blues')
pd.plotting.scatter_matrix(iris, c=iris.species_num)
plt.show()
