# Model Evaluation Procedures

'''Last time, we created classification models on the iris data to predict species using 
the iris measurements. We used KNN, with K=1 and K=5. But which model is better? And more 
importantly, what's the best value of K? 
'''

'''To choose between models, we need two things:

1. Evaluation procedure: the process you use to evaluate a model
2. Evaluation metric: the numeric calculation you use to compare models

In supervised learning, we define the "best" model as one that generalizes to 
"out-of-sample" data. In other words, we want a model that accurately predicts the 
future, not the past. Our evalutaion procedure should support that goal.

Choosing an evaluation metric is a more subjective decision. The appropriate evaluation
metric can depend upon the goal of your problem. We will focus on evaluation metrics in 
future class.'''


# Evaluation Procedure 1: Train and Test on Entire Dataset

# read in the iris data
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier # import class
from sklearn.datasets import load_iris
iris = load_iris()

# create X (features) and y (response)
X = iris.data
y = iris.target

# KNN with K=5
knn = KNeighborsClassifier(n_neighbors=5)  # instantiate the estimator
knn.fit(X, y)  # train on entire dataset
y_pred = knn.predict(X)  # make predictions

'''Let's compute the accuracy. This is known as training accuracy because we are testing
on the same data we used to train the model.'''

# method 1: use metrics module
print(metrics.accuracy_score(y, y_pred))

# method 2: use NumPy
print(np.mean(y == y_pred))

# method 3: use the built-in "score" method
print(knn.score(X, y))

'''I recommend method 1 because this pattern can be reused for different evaluation 
metrics'''

# now try KNN with K=1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
y_pred = knn.predict(X)
print(metrics.accuracy_score(y, y_pred))

'''Training accuracy rewards overly complex models that do  not generalize to out-of-sample
data. Setting K=1 caused KNN to effectively memorize the training data. Thus, it will do very
well when tested using the in-sample data, by may do very poorly on out-of-sample data. As such
, training accuracy is not good estimate of out-of-sample accuracy, and out-of-sample accuracy
is what matters.

Creating an unnecessarily complex model is known as overfitting, because it is learning the
"noise" rather than the "signal".'''

# Evaluation Procedure 2: Train/Test Split

# 1. Split the dataset into two pieces: a training set and a testing set
# 2. Train the model on the training set
# 3. Test the model on the testing set, and evaluate how well we did
# 4. Repeat steps 2 and 3 using different tuning parameters

# we are evaluating the model on data that was not used to train the model

# create X: 5 observations and 2 features
X = np.arange(1, 11).reshape((5, 2))
print(X)

# create y: resonse vector of size 5
y = X.prod(axis=1)
print(y)

# randomly split the rows of X into two pieces
X_split = train_test_split(X)  # returns a list with two elements
print(X_split[0])
print(X_split[1])

# use random_state parameter to always get the same random split
X_split = train_test_split(X, random_state=2)
print(X_split[0])
print(X_split[1])

# "unpack" the list into two separate objects
X_train, X_test = train_test_split(X, random_state=2)
print(X_train)
print(X_test)

# randomly split the rows of X and y into two pieces each
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)

# X has been split into two pieces
print(X_train)
print(X_test)

# y has been split into two pieces with the same ordering
print(y_train)
print(y_test)

# Using the Train/Test split procedure on iris

# step 0 load the iris data again
iris = load_iris()
X = iris.data
y = iris.target

# step 1 split data into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# step 2 train the model on the training set (using K=1)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# step 3 test the model on the testing set, and check accuracy
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

# step 4 repeat this process for K=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

'''K=1 had a higher training accuracy than K=5, but K=5 had a higher testing accuracy
than K=1. Testing accuracy is a much better estimator of out-of-sample accuracy, and thus 
we would prefer to use K=5 in this situation.

We would declare 5 to be the best value for K when using KNN on the iris dataset. We would
estimate that when given the measurement of an unknown iris, we would be able to correctly
predict its species 97% of the time.
'''

# Making predictions on out-of-sample data

''' We are now given the measurements of a truly unknown iris, and are asked to predict its 
species. How do we do it?

1. We re-train our model on the entire dataset, using the best value  for K found in the 
previous step.
2. We make our prediction, and are 97% sure that we will make the correct prediction. 

It is important to re-train your model on all of the data, otherwise you will be
ignoring valuable training data.'''

# train the model on X (not X_train) using K=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# make a prediction for an unknown iris
out_of_sample = [[5, 4, 3, 2]]
print(knn.predict(out_of_sample))
