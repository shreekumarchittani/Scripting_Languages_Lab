import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanictrain.csv')
print(df.head())
print(df.describe())
df.drop(['Ticket','Embarked'],axis=1)
df['Cabin'] = df['Cabin'].fillna('Null')
print(df['Cabin'])
ax = sns.barplot(x='Pclass',y='Survived',data=df)
plt.show()