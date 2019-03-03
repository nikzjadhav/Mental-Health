import Main as t
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from subprocess import check_output
survey=t.df
survey['Gender'] = survey['Gender'].str.lower()
male = ["male", "m", "male-ish", "maile", "mal", "male (cis)", "make", "male ", "man","msle", "mail", "malr","cis man", "cis male"]
trans = ["trans-female", "something kinda male?", "queer/she/they", "non-binary","nah", "all", "enby", "fluid", "genderqueer", "androgyne", "agender", "male leaning androgynous", "guy (-ish) ^_^", "trans woman", "neuter", "female (trans)", "queer", "ostensibly male, unsure what that really means"]
female = ["cis female", "f", "female", "woman",  "femake", "female ","cis-female/femme", "female (cis)", "femail"]
survey['Gender'] = survey['Gender'].apply(lambda x:"Male" if x in male else x)
survey['Gender'] = survey['Gender'].apply(lambda x:"Female" if x in female else x)
survey['Gender'] = survey['Gender'].apply(lambda x:"Trans" if x in trans else x)
survey.drop(survey[survey.Gender == 'p'].index, inplace=True)
survey.drop(survey[survey.Gender == 'a little about you'].index, inplace=True)



plt.figure(figsize=(10,5))
sns.countplot(y="Gender", hue="treatment", data=survey)
plt.title("Mental health wrt Gender",fontsize=18,fontweight="bold")
plt.ylabel("")

plt.savefig('fig\HealthwrtGender.jpg')
plt.show()