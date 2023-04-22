from google.cloud import bigquery
client = bigquery.Client()

class TestClass:
    def test_hello_world(self):
        x = "hello world"
        assert "hello" in x

    question_1 = client.query("""SELECT * FROM foodpanda-de-test-sharon.staging.question_1""")
    question_1.result()

    def test_question_1_table_length(self, query_job=question_1): 
        dict_query = dict(query_job)
        assert len(dict_query) == 5
