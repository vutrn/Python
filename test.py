import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train_df = pd.read_csv('titanic/train.csv')
test_df = pd.read_csv('titanic/test.csv')

print(train_df.columns)
print(train_df.head())

print(plt.show(train_df))