import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Dataset.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
z = dataset.iloc[[2]].values

dataset.info()

dataset.isnull().sum()

dataset.isnull().sum().sum()

print(z)

print(x)

print(y)

