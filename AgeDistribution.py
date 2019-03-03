import Main as t
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from subprocess import check_output

fig,ax = plt.subplots(figsize=(8,6))
sns.distplot(t.df['Age'].dropna(),ax=ax,kde=True,rug=True,color='#1e8dec')
s="" +str(t.df['Age'].describe())
plt.text(40,0.05,s);
plt.title('Age Distribution')
plt.ylabel('Freq')
#plt.grid()
plt.savefig('fig\AgeDistribution.jpg')
plt.show()