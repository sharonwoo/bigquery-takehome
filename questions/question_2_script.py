from google.cloud import bigquery
from settings import bigquery_project

'''
Question:   Which country has the largest number of ports with a cargo_wharf?
            Your answer should include the columns country and port_count only.
Answer:     US
Design choice:
        return only 1 row with columns stating country and port_count only
Notes & assumptions:
        1. cargo wharf can take values of true, false, or null (2787, 7, 875).
            we assume only true values are ports with cargo wharves
        2. assumption: duplicated port names are unique ports.
            there are duplicates by port_name in US, CA, ID, AR
            but they have different column values and different indexes
            e.g. in AR, VILLA CONSTITUCION port name is duplicated but
            there are slight differences to the latlong,
            and differences in the index number which is one of our clustering
            columns, so we assume it's different

'''


def main(bigquery_project=bigquery_project):
    client = bigquery.Client()

    table_id = "{bigquery_project}.staging.question_2".format(
                                    bigquery_project=bigquery_project)

    job_config = bigquery.QueryJobConfig(destination=table_id,
                                         write_disposition="WRITE_TRUNCATE")

    sql = """
        WITH cargo_wharves AS (
            SELECT
                port_name,
                country,
                cargo_wharf
            FROM `bigquery-public-data.geo_international_ports.world_port_index`
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

    print("The query data:")
    for row in query_job:
        print(row)


if __name__ == '__main__':
    main()
