import Main as t

import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from subprocess import check_output
fig,ax = plt.subplots(figsize=(8,6))
sns.countplot(t.df['Country']);
plt.xticks(rotation='vertical');
plt.savefig('fig\All_country.jpg')
plt.show()
