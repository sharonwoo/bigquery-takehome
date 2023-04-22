# bigquery-takehome
make pink home again (now with rudimentary cicd)

## Answers to take home

* [question 1 script](https://github.com/sharonwoo/bigquery-takehome/blob/main/questions/question_1_script.py)
* [question 2 script]((https://github.com/sharonwoo/bigquery-takehome/blob/main/questions/question_2_script.py))
* [question 3 script]((https://github.com/sharonwoo/bigquery-takehome/blob/main/questions/question_3_script.py))
* [question 4 markdown]
* [question 5 markdown]
* [BigQuery project](https://console.cloud.google.com/bigquery?project=foodpanda-de-test-sharon&ws=!1m4!1m3!3m2!1sfoodpanda-de-test-sharon!2sstaging)

## How this repo is meant to be used by anyone

1. Make a pull request which has a branch name prefixed with `dev/` to modify the questions in the `questions` folder. For Q1-Q3 scripts, modifying any of them will create new tables for all 3 in `staging`.
2. Make sure the tests pass. 
3. @sharonwoo will review the code before it can be merged to `main`. Upon doing so, Q1-Q3 tables will be created in `production`. 

I also considered other use cases: 

### Fork this repo

1. Update your `GOOGLE_APPLICATION_CREDENTIALS` in the repository secret with your own service account credentials.
2. 

### If you really have to run the Python scripts locally

No guarantees it'll work, but I assume you have Python 3.10 or later installed and that you have (configured gcloud CLI)[https://cloud.google.com/sdk/docs/initializing].

```
# see venv docs: https://docs.python.org/3/library/venv.html
# create a virtual environment 
python -m venv /path/to/new/virtual/environment

# activate virtual environment in zsh shell
source <venv>/bin/activate

# install requirements.txt
pip install -r requirements.txt

# change bigquery_project in questions/settings.py
bigquery_project = 'your-project-name-here'

# try running the scripts and test
python questions/question_1_script.py
pytest tests/test_questions.py

```

## Requirements & design choices

| Requirement   | Design choice        |
| ---           | ---                  |
| complete this exercise in Python | [use Python client](https://cloud.google.com/python/docs/reference/bigquery/latest), use the boilerplate code without refactoring first although not strictly required (e.g. for table_id, job_configs) |
| create a public Github repository to store any code and your progress | use Github Actions to create tables in BigQuery `staging` dataset and `production` dataset, also so you don't have to peep my `.git` folder omg |
| repository should also indicate how any other user can use it | TBC - plan is to have any user submit a PR to create a table in staging, and then only @sharonwoo can approve PRs to create tables in production. Also going to DRY out code so it can be used locally by anyone else |
| Q1-Q3: create a script which follows good software engineering practices that creates a BigQuery table in your personal Google Cloud Project | script uses Github Actions to write a staging table upon push to any `dev/*` branch updating a question script python file. also write some automated tests to check the requirements for tables are fulfilled. | 
| Q4 what are tests and refactoring? | Possibly overdo it by writing both tests and baking refactoring into the assignment, with  to show, not tell (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ |
| Q5 look at FastAPI and suggest improvements | Clean up PRs, @tiangolo pls, [also](https://github.com/zhanymkanov/fastapi-best-practices#6-follow-the-rest) [what](https://github.com/tiangolo/fastapi/discussions/9412)|