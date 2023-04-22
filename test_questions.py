from google.cloud import bigquery
client = bigquery.Client()



class TestHelloWorld:
    def test_hello_world(self):
        x = "hello world"
        assert "hello" in x

class TestQuestion1:
    question_1 = client.query("""SELECT * FROM foodpanda-de-test-sharon.staging.question_1""")
    question_1.result()

    '''
        question 1 constraints: 
            5 nearest ports
            columns port_name and distance_in_meters only
    '''

    def test_question_1_table_total_rows(self, query_job=question_1): 
        dict_query = dict(query_job)
        assert len(dict_query) == 5

    def test_question_1_table_total_columns(self, query_job=question_1): 
        assert len(question_1._query_results._properties['schema']['fields']) == 2

    def test_question_1_column_names(self, query_job=question_1): 
        # get column names from properties 
        # https://stackoverflow.com/questions/55757039/how-to-get-column-name-from-bigquery-api
        # [{'name': 'port_name', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'distance_in_meters', 'type': 'FLOAT', 'mode': 'NULLABLE'}]
        # this also implicitly tests ordering. if no ordering is desired, use a set
        assert question_1._query_results._properties['schema']['fields'][0]['name'] == 'port_name'
        assert question_1._query_results._properties['schema']['fields'][1]['name'] == 'distance_in_meters'
    
class TestQuestion2:
    question_2 = client.query("""SELECT * FROM foodpanda-de-test-sharon.staging.question_2""")
    question_2.result()
    '''
        question 2 constraints: 
            return "which country has largest", so 1 row in size
            columns country and port_count only
    '''

    def test_question_2_table_total_rows(self, query_job=question_2): 
        dict_query = dict(query_job)
        assert len(dict_query) == 1

    def test_question_2_table_total_columns(self, query_job=question_2): 
        assert len(question_2._query_results._properties['schema']['fields']) == 2

    def test_question_2_column_names(self, query_job=question_2): 
        assert question_2._query_results._properties['schema']['fields'][0]['name'] == 'country'
        assert question_2._query_results._properties['schema']['fields'][1]['name'] == 'port_count'

class TestQuestion3:
    question_3 = client.query("""SELECT * FROM foodpanda-de-test-sharon.staging.question_3""")
    question_3.result()
    '''
        question 3 constraints: 
            return "nearest port", so 1 row in size
            columns country, port_name, port_latitude and port_longitude only
    '''

    def test_question_2_table_length(self, query_job=question_3): 
        dict_query = dict(query_job)
        assert len(dict_query) == 1

    def test_question_2_table_total_columns(self, query_job=question_3): 
        assert len(question_2._query_results._properties['schema']['fields']) == 2

    def test_question_3_column_names(self, query_job=question_3): 
        assert question_3._query_results._properties['schema']['fields'][0]['name'] == 'country'
        assert question_3._query_results._properties['schema']['fields'][1]['name'] == 'port_name'
        assert question_3._query_results._properties['schema']['fields'][2]['name'] == 'port_latitude'
        assert question_3._query_results._properties['schema']['fields'][3]['name'] == 'port_longitude'