from google.cloud import bigquery
import os

# Setting configs
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'

# Create a big query client
bigquery_client = bigquery.Client()

# Create a dataset called test_dataset
bigquery_client.create_dataset('test_dataset')

table_id = 'sincere-strata-364512.test_dataset.test_table'

# Creating a new table called: test_table
bigquery_client.create_table(table=table_id)


job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("event_id", "INTEGER"),
            bigquery.SchemaField("event_timestamp", "DATETIME"),
            bigquery.SchemaField("event_name", "STRING")
        ],
        skip_leading_rows=1,
        # The source format defaults to CSV, so the line below is optional.
        source_format=bigquery.SourceFormat.CSV
    )
uri = "https://storage.cloud.google.com/chapter_4/full_extract_mongodb/event_logs.csv"

load_job = bigquery_client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = bigquery_client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))
# [END bigquery_load_table_gcs_csv]
