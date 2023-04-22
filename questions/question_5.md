# Question 5

> Have a browse of https://github.com/tiangolo/fastapi and write down how this repository is structured and why. What improvements do you think can be made?

Possibly useful context: I've not actually used FastAPI before but have studied it and elected to use Django/drf over it and Flask for a previous exercise creating a backend API because Django/drf was very batteries-included and I found easier to use. 

## How repository is structured 

![fastapi](/images/fastapi.png)

* `.github` contains configuration files for Github Actions, which includes (but isn't exhaustive)
    * Discussion templates and issue templates - this is neat because it separates issues (for genuine issues), discussions (for help) and PRs
    * Funding 
    * Automated tests (why is this written as a bash script that invokes pytest?)
    * Documentation builder
* `docs` contains part of the material - the text and article structure - for https://fastapi.tiangolo.com e.g. https://github.com/tiangolo/fastapi/blob/master/docs/en/docs/features.md maps to https://fastapi.tiangolo.com/features/. The sidebar on the site inherits the structure of this folder. 
* `docs_src` contains the code snippets used in the `docs` article, e.g. https://fastapi.tiangolo.com/advanced/graphql/?h=graphql contains the snippet https://github.com/tiangolo/fastapi/blob/master/docs_src/graphql/tutorial001.py
* `fastapi` contains the code for the framework. 
* `scripts` looks like it contains bash cripts used in Github Actions; about half of these have not been updated for 3-4 years. 
* `tests` contains a very, very large suite of pytest tests; many of these have not been updated for 3-4 years. Looking at a [sample merged PR](https://github.com/tiangolo/fastapi/pull/9315/checks) there are over 1,900 tests, about 500 of which are skipped in a run. 

## Improvements that can be made 

* Triage stale pull requests - there are over 400 open as of right now, most of which are over a year old. This might require additional reviewers - lots of PRs are tagged `awaiting review`. 
    * Many PRs are related to translations and documentation and do not appear to directly impact API functionality. 
    * Because there are so many outstanding PRs, it's hard to see what new functionality is being added, what needs to be fixed etc. 
    * Looking at PRs that are merged, @tiangolo appears to only be updating sponsor-related information and some submitted smal fixes around once a month. This is pretty demoralising if an issue is found and there may not be a fix for some time. 
* Readme.md improvement: shorten, tighten focus. 
    * At a glance, the `readme` covers where to find the documentation and source code, as well as which versions of Python it supports. This is great for developers. 
    * It then segues into developer opinions and sponsors as well as reasons for use, which I understand might be important for continued funding, but which I found confusing. 
    * It even advertises Typer which is something that might be new - don't remember this being there last year. 
* Consolidate `docs` and `docs_src` folders into 1 folder (which might need some refactoring)
