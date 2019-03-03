import Main as t
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=t.df
df['Age_Group'] = pd.cut(t.df['Age'].dropna(),
                         [0,18,25,35,45,99],
                         labels=['<18','18-24','25-34','35-44','45+'])

fig,ax = plt.subplots(figsize=(8,6))
sns.countplot(data=df,x = 'Age_Group',hue= 'family_history',ax=ax)
plt.title('Age vs family_history')

plt.savefig('fig\AgeVsHistory.jpg')
plt.show()