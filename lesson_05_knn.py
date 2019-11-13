import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
col_names = ['sepal_lenght', 'sepal_width',
             'petal_lenght', 'petal_widht', 'species']
iris = pd.read_csv('iris.data', names=col_names)

# create numeric column for the response
# note: features and response must both be entirely numeric!

iris['species_num'] = iris.species.map(
    {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})
print(iris.shape)
print(iris.columns)

# create X features three different ways

feature_columns = ['sepal_lenght',
                   'sepal_width', 'petal_lenght', 'petal_widht']

X = iris[feature_columns]
X = iris.loc[:, 'sepal_lenght':'petal_widht']
X = iris.iloc[:, 0:4]

# create y response vector
y = iris.species_num

# check the shape of X and y
print(f"features: {X.shape} and response: {y.shape}")

'''
Scikit-Learn 4-step modeling pattern:
'''

# Step 1: import the class you plan to use

# Step 2: instantiate the "estimator" (aka the model)
# note: all unspecified parameters are set to the defaults

knn = KNeighborsClassifier(n_neighbors=1)

# Step 3: fit the model with data (learn the relationship between X and y)
knn.fit(X, y)

# Step 4: use the "fitted model" to predict the response for a new observation

print(knn.predict([[3, 5, 4, 2], ]))
# predict for multiple observations at once
X_new = [[3, 5, 4, 2], [3, 5, 2, 2]]
print(knn.predict(X_new))


# try a different value of K ("tuning parameter")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
print(knn.predict(X_new))
print(knn.predict_proba(X_new))
print(knn.kneighbors([[3, 5, 4, 2], ]))

# calculate Euclidean distance manually for nearest neighbor
print(np.sqrt(((X.iloc[106, :] - [3, 5, 4, 2])**2).sum()))
