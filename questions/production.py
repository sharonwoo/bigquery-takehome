from google.cloud import bigquery
from settings import bigquery_project


def question_template(question):
    client = bigquery.Client()
    staging_table_id = "{bigquery_project}.{dataset}.{question}".format(
                                    dataset='staging',
                                    bigquery_project=bigquery_project,
                                    question=question)
    production_table_id = "{bigquery_project}.{dataset}.{question}".format(
                                    dataset='production',
                                    bigquery_project=bigquery_project,
                                    question=question)

    job_config = bigquery.QueryJobConfig(destination=production_table_id,
                                    write_disposition="WRITE_TRUNCATE")

    sql = "SELECT * FROM {staging_table_id}".format(
                                    staging_table_id=staging_table_id)

    query_job = client.query(sql, job_config=job_config)
    query_job.result()

    print("Query results loaded to the table {}".format(production_table_id))


if __name__ == '__main__':
    question_template(question='question_1')
    question_template(question='question_2')
    question_template(question='question_3')
