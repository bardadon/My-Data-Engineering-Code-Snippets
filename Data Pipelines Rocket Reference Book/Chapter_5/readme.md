# Loading Data - Prerequisites and Introduction

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

![Untitled(42)](https://user-images.githubusercontent.com/65648983/194718655-74340949-140f-4f1c-a803-01b2530fe8b6.png)

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

![Untitled(43)](https://user-images.githubusercontent.com/65648983/194718695-cf5025d8-d48b-432c-8664-f3adf4413728.png)

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
![Untitled(45)](https://user-images.githubusercontent.com/65648983/194718724-14a89c08-fb47-481e-9d34-e63e90dd161c.png)

