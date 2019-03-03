import numpy as np
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'H:/Workspace_py/Project/input/mental-health-data-910dace24efa.json')
project_id = 'mentalhealth9911'
client = bigquery.Client(credentials= credentials,project=project_id)

query_job = client.query("""
  SELECT * FROM `mentalhealth9911.healthsurvey.healthsurvey` """)

results = query_job.result()

query_new = client.query("""
  SELECT distinct Country FROM `mentalhealth9911.healthsurvey.healthsurvey` """)

country=query_new.result()
df2 = country.to_dataframe()
print("Total Country ",df2.head(100))

df = results.to_dataframe()
df.head()

print(df.info())

df['Age'] = pd.to_numeric(df['Age'],errors='coerce')

def age_process(age):
    if age>=0 and age<=100:
        return age
    else:
        return np.nan

df['Age']=df['Age'].apply(age_process)

