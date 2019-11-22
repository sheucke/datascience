import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_table('../data/x01.txt', sep='\s+', skiprows=33,
                   names=['id', 'brain', 'body'], index_col='id')

print(df.head())

print(df.describe())

# filter on body weight less than 200 to focus on smaller subset

df = df[df.body < 200]
print(df.shape)

# create a scatterplot (using Seaborn) to visulize the relationship between brain and body
# weight:

sns.lmplot(x='body', y='brain', data=df, ci=None, fit_reg=False)
plt.xlim(-10, 200)
plt.ylim(-10, 250)
plt.show()

sns.lmplot(x='body', y='brain', data=df, ci=None)
sns.set(style="whitegrid", font_scale=1.5)
plt.xlim(-10, 200)
plt.ylim(-10, 250)
plt.show()

# set a random seed for reproducubility
np.random.seed(12345)

# randomly assign every row to either sample 1 or sample 2
df['sample'] = np.random.randint(1, 3, len(df))
print(df.head())

# use seaborn to create two plots, in which the left plot only uses the data from sample 1
# and the right plot only uses the data from sample 2:

# col='sample' subsets the data by sample and creates two separate plots
sns.lmplot(x='body', y='brain', data=df, ci=None, col='sample')
plt.xlim(-10, 200)
plt.ylim(-10, 250)
plt.show()

# hue='sample' subsets the data by color and create a single plot

sns.lmplot(x='body', y='brain', data=df, ci=None, hue='sample')
plt.xlim(-10, 200)
plt.xlim(-10, 250)
plt.show()

# The above is a visual demonstration of a high bias, low variance model
# It's high bias because it doesn't fit the data particularly well.
# It's low variance because it doesn't chance much depending upon which points
# happen to be in the sample

# next is a low bias, high variance model
# polynomial regression, with an eight order polynomial:

sns.lmplot(x='body', y='brain', data=df, ci=None,
           col='sample', order=8)  # ci = confidence intervall
plt.xlim(-10, 200)
plt.ylim(-10, 250)
plt.show()

# It's low bias because the model match the data quite well
# It's high variance because the models are widely different depending upon which
# points happen to be in the sample.

# find a middle ground
# create a second order polynomial model, that has less bias than the linear model, and
# less variance then the eighth order polynomial

sns.lmplot(x='body', y='brain', data=df, ci=None, col="sample", order=2)
plt.xlim(-10, 200)
plt.ylim(-10, 250)
plt.show()

# This seems better. In both the left and right plots, it fits the data pretty well,
# but not to well.
# This is the essence of the bias-variance tradeoff: finding a model that appropriately
# balances bias  and variance, and thus will generalize to new data (known as "out of sample")
