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

Question:       What are the 5 nearest ports to Singapore's JURONG ISLAND port? (country = 'SG', port_name = 'JURONG ISLAND')
                Your answer should include the columns port_name and distance_in_meters only.
Design choice:  use LIMIT 5 to limit to 5 results
Notes & assumptions:          
                1. assumption: duplicated port names are unique ports (see question_2_script.py notes for full reasoning)

'''

client = bigquery.Client()

table_id = "foodpanda-de-test-sharon.staging.question_1"

# set write_truncate for testing; if necessary append author name to version tables if multiple contributors?
job_config = bigquery.QueryJobConfig(destination=table_id, write_disposition="WRITE_TRUNCATE")

sql = """
    WITH geopoints AS (
        SELECT 
            port_name, 
            port_geom, 
        FROM    `bigquery-public-data.geo_international_ports.world_port_index` 
        WHERE   DATE(_PARTITIONTIME) >= "2019-09-24" ) -- Sep 24, 2019
        , 

        jurong_island AS (
        SELECT 
            port_name,
            port_geom as jurong_island
        FROM    geopoints
        WHERE   port_name = 'JURONG ISLAND'
        ), 

        dataset AS (
        SELECT 
            geopoints.port_name,
            geopoints.port_geom,
            jurong_island.jurong_island 
        FROM        geopoints
        LEFT JOIN   jurong_island
               ON   geopoints.port_name <> jurong_island.port_name
        )

    SELECT 
        port_name, 
        ST_DISTANCE(port_geom, jurong_island) as distance_in_meters
    FROM    dataset
    WHERE   port_name != 'JURONG ISLAND'
    ORDER BY distance_in_meters ASC 
    LIMIT 5
"""

query_job = client.query(sql, job_config=job_config) 
query_job.result()

print("Query results loaded to the table {}".format(table_id))

# can use QueryJob row iterator results to write tests later
# now, to print out the table results so no need to check in BQ
print("The query data:")
for row in query_job:
    print(row)