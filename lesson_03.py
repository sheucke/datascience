"""
Pandas for Data Exploration, Analysis, and Visualization
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

drinks = pd.read_table('../data/drinks.csv')
print(drinks.head())
