# bigquery-takehome
make pink home again (now with rudimentary cicd)

| Requirement   | Design choice        |
| ---           | ---                  |
| complete this exercise in Python | [use Python client](https://cloud.google.com/python/docs/reference/bigquery/latest), use the boilerplate code without refactoring first although not strictly required (e.g. for table_id, job_configs) |
| create a public Github repository to store any code and your progress | use Github Actions to create tables in `staging` and `production` |
| repository should also indicate how any other user can use it | TBC - plan is to have any user submit a PR to create a table in staging, and then only @sharonwoo can approve PRs to create tables in production. Also going to DRY out code so it can be used locally by anyone else |
| Q1-Q3: create a script which follows good software engineering practices that creates a BigQuery table in your personal Google Cloud Project | script uses Github Actions to write a staging table upon push to any `dev/*` branch updating a question script python file | 
