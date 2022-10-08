# Chapter 5 - Loading Data

The author of the book is using Amazon Redshift. He is connecting his s3 bucket to redshift to transfer data between them.

I should do the same using Google bucket and Google BigQuery(Check if its free in the free tier).

Lets see how to pull data from google Big Query

```python
pip install google-cloud-bigquery
```

Now lets connect and create a dataset and a table in google big query:

```python
from google.cloud import bigquery

# Setting configs
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'

# Create a big query client
bigquery_client = bigquery.Client()

# Create a dataset called test_dataset
bigquery_client.create_dataset(table='test_dataset')
```

Now to create a table, grab the project id:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ca812d04-6854-403d-9997-b53132315c1a/Untitled.png)

And add it like this: <ProjectId>.<DataSet>.<NewTableName>

```python
# Creating a new table called: test_table
bigquery_client.create_table(table='sincere-strata-364512.test_dataset.test_table')
```

Now the code to grab a csv file from the bucket and load it into big query is this:

```python
from google.cloud import bigquery

# Setting configs
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'

# Construct a BigQuery client object.
client = bigquery.Client()

table_id = 'sincere-strata-364512.test_dataset.test_table'

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

load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))
# [END bigquery_load_table_gcs_csv]
```

Notes:

1. Grab the table id according to what is shown above.
2. uri  —> Go to the bucket, click on the csv file and copy the URL.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0b136f6f-b474-4604-af01-6555b25e1be9/Untitled.png)

1. Make sure that the datatypes are suitable for what is in the CSV file.

The entire code looks like this:

```python
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
```

End result

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/68c9c3e9-9d3d-405a-a5b2-3a198a22a8ac/Untitled.png)
