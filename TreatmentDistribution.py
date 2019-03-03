import Main as t
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=t.df
df['Timestamp'] = t.pd.to_datetime(df['Timestamp'],format='%Y-%m-%d')
df['Year'] = df['Timestamp'].apply(lambda x:x.year)
sns.countplot(df['treatment'])
plt.title('Treatement Distribution')


plt.savefig('fig\TreatmentDistribution.jpg')
plt.show()