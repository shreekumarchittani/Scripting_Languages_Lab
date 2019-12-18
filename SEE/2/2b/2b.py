import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('student.csv')
'''print(df.head)
print(df.describe())
df = df.drop(['lunch','test preparation course'],axis=1)
print(df)'''
df['parental level of education'] = df['parental level of education'].fillna('Null')
print(df)
ax = sns.countplot(x='test preparation course',hue='gender',data=df)
plt.show()