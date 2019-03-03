import Main as t
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from subprocess import check_output

country_count=Counter(t.df['Country'].dropna().tolist()).most_common(10)
country_index=[country[0] for country in country_count]
conuntry_val=[country[1] for country in country_count]
fig,ax=plt.subplots(figsize=(10,6))
sns.barplot(x=country_index,y=conuntry_val,ax=ax)
plt.title('Top ten country')
plt.xlabel('Country')
plt.ylabel('Count')
ticks = plt.setp(ax.get_xticklabels(),rotation=90)

plt.savefig('fig\Toptencountry.jpg')
plt.show()