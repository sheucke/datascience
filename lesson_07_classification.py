import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
df = pd.read_csv('../data/glass.data',
                 names=['id', 'ri', 'na', 'mg', 'al', 'si',
                        'k', 'ca', 'ba', 'fe', 'glass_type'],
                 index_col='id')


# explore the data
print(df.shape)
print(df.head())
print(df.tail())
print(df.glass_type.value_counts())
print(df.isnull().sum())

# convert to binary classification problem (1/2/3/4 to 0, 5/6/7 to 1)
df['binary'] = np.where(df.glass_type < 5, 0, 1)
df['binary'] = df.glass_type.map({1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 1})
print(df.binary.value_counts())

# create a feature matrix (X)
features = df.columns[:-2]
X = df[features]

# create a response vector (y)
y = df.binary

# split X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=99)

# fit a KNN model on the training set using K=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# make predictions on the testing set and calculate accuracy
y_pred = knn.predict(X_test)
print(accuracy_score(y_test, y_pred))

#  calculate null accuracy
print(1 - y.mean())

# write a for loop that compute test set accuracy for a range of K values
k_range = range(1, 30, 2)
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(accuracy_score(y_test, y_pred))

print(scores)

# plot K versus test set accuracy to choose on optimal value for K
plt.plot(k_range, scores)
plt.show()
