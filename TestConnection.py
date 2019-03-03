from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
    'H:/Workspace_py/Project/input/mental-health-data-910dace24efa.json')
project_id = 'mentalhealth9911'
client = bigquery.Client(credentials= credentials,project=project_id)
print("Hello")


query_job = client.query("""
  SELECT * FROM `mentalhealth9911.healthsurvey.healthsurvey` LIMIT 1000""")
results = query_job.result()

'''for row in results:
    print("{} : {} ".format(row.Age, row.Gender))
'''
df = results.to_dataframe()
df.head()


