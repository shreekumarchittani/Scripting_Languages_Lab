import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('IRIS.csv')
print(df.head())
print(df.describe())
print(df[['species','petal_width']].groupby(['species'],as_index=True).mean())
ax = sns.countplot(x='species',hue='sepal_width',data=df)
plt.show()