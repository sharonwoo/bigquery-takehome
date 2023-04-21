from google.cloud import bigquery

'''
Requirement:    complete this exercise in Python
Design choice:  use Python client, https://cloud.google.com/python/docs/reference/bigquery/latest
                source code to figure out how to write tests later: https://github.com/googleapis/python-bigquery
                use the boilerplate code without refactoring first; can create utility functions and classes later if time/ocd permits although not strictly required (e.g. for table_id, job_configs)
                also need to figure out linting if time permits

Requirement:    create a public Github repository to store any code and your progress
Design choice:  use Github Actions to create tables

Requirement:    repository should also indicate how any other user can use it
Design choice:  TBC - plan is to have any user submit a PR to create a table in staging, and then only @sharonwoo can approve PRs to create tables in production

Requirement:    create a script which follows good software engineering practices that creates a BigQuery table in your personal Google Cloud Project
Design choice:  this script uses Github Actions to write the table upon push to dev/*

*______*

Question:       Which country has the largest number of ports with a cargo_wharf? Your answer should include the columns country and port_count only.
Answer:         US
Design choice: return only 1 row with columns stating country and port_count only
Notes & assumptions:          
                1. cargo wharf can take values of true, false, or null (2787, 7, 875). we assume only true values are ports with cargo wharves
                2. assumption: duplicated port names are unique ports. 
                   there are duplicates by port_name in US, CA, ID, AR but they have different column values and different indexes
                   e.g. in AR, VILLA CONSTITUCION port name is duplicated but there are slight differences to the latlong, 
                   and differences in the index number which is one of our clustering columns, so we assume it's different

'''

client = bigquery.Client()

table_id = "foodpanda-de-test-sharon.staging.question_1"

# set write_truncate for testing; if necessary append author name to version tables if multiple contributors?
job_config = bigquery.QueryJobConfig(destination=table_id, write_disposition="WRITE_TRUNCATE")

sql = """
    WITH cargo_wharves AS (
        SELECT 
            port_name,
            country,
            cargo_wharf
        FROM  `bigquery-public-data.geo_international_ports.world_port_index` 
        WHERE DATE(_PARTITIONTIME) = "2019-09-24"
        AND   cargo_wharf = true
    )

    SELECT
        country,
        count(port_name) as port_count
        FROM cargo_wharves
    GROUP BY 1
    ORDER BY port_count DESC
    LIMIT 1
"""

query_job = client.query(sql, job_config=job_config) 
query_job.result()

print("Query results loaded to the table {}".format(table_id))

# can use QueryJob row iterator results to write tests later
# now, to print out the table results so no need to check in BQ
print("The query data:")
for row in query_job:
    print(row)