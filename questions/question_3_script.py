from google.cloud import bigquery
from settings import bigquery_project

'''
Question:   You receive a distress call from the middle of the North Atlantic
            Ocean. The person on the line gave you a coordinates of
            lat: 32.610982, long: -38.706256 and asked for the nearest port
            with provisions, water, fuel_oil and diesel.
            Your answer should include the columns country,
            port_name, port_latitude and port_longitude only.
Answer:     HORTA is the name of the nearest port, please see tables for rest
Design choice: return only 1 row with requested columns only
Notes & assumptions:
            1. provisions, water, fuel_oil and diesel can take values of true,
            false, or null (2787, 7, 875).
            we assume only true values represent ports which have any of these
            2. assumption: duplicated port names are unique ports
            (see question_2_script.py for working)
'''


def main(bigquery_project=bigquery_project):
    client = bigquery.Client()

    table_id = "{bigquery_project}.staging.question_3".format(
                                    bigquery_project=bigquery_project)

    job_config = bigquery.QueryJobConfig(destination=table_id,
                                         write_disposition="WRITE_TRUNCATE")

    sql = """
        WITH geopoints AS (
            SELECT
                country,
                port_name,
                port_geom,
                port_latitude,
                port_longitude,
                provisions,
                water,
                fuel_oil,
                diesel
            FROM    `bigquery-public-data.geo_international_ports.world_port_index`
            WHERE   DATE(_PARTITIONTIME) = "2019-09-24"
        ),

        distress_call AS (
            SELECT
                'DISTRESS CALL' as port_name,
                ST_GEOGPOINT(-38.706256, 32.610982) as distress_call
        ),

        dataset AS (
            SELECT
                geopoints.*,
                distress_call.distress_call
            FROM      geopoints
            LEFT JOIN distress_call
                ON geopoints.port_name <> distress_call.port_name
        ),

        all_ports_by_distance AS (

        SELECT
            dataset.* EXCEPT(port_geom, distress_call),
            ST_DISTANCE(port_geom, distress_call) as distance_in_meters
        FROM dataset
        ORDER BY distance_in_meters ASC
        )

        SELECT
            country,
            port_name,
            port_latitude,
            port_longitude
        FROM all_ports_by_distance
        WHERE (provisions AND water AND fuel_oil AND diesel)
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
