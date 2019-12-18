import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('BlackFriday.csv')
print(df.head())
print(df.describe())
df['City_Category'] = df['City_Category'].fillna('B')
print(df['City_Category'])
df['City_Category'] = df['City_Category'].map({
    'A':'Metro',
    'B':'Small Towns',
    'C':'Villages'
})
ax = sns.countplot(x='Gender',hue='City_Category',data=df)
plt.show()
