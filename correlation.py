from sklearn.preprocessing import LabelEncoder
import Main as t
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from subprocess import check_output
import numpy as np
survey=t.df
number = LabelEncoder()
for i in survey.columns:
    survey[i] = number.fit_transform(survey[i].astype('str'))

corr=survey.corr()['treatment']
corr[np.argsort(corr,axis=0)[::-1]]

features_correlation = survey.corr()
plt.figure(figsize=(8,8))
sns.heatmap(features_correlation,vmax=1,square=True,annot=False,cmap='Blues')
plt.savefig('fig\Correlation.jpg')
plt.show()