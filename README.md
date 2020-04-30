# flasklogin_neo4j
Implementing Flask Login with Neo4j

# Dependencies
![Python](https://img.shields.io/badge/Python-v3.7-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v1.1.1-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Login](https://img.shields.io/badge/Flask--Login-v0.4.1-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Assets](https://img.shields.io/badge/Flask--Assets-v0.12-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![WTForms](https://img.shields.io/badge/WTForms-v2.2.1-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Assets](https://img.shields.io/badge/Py2neo--v4.30-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)

_This project is an implementation of [Flask Login](https://flask-login.readthedocs.io/en/latest/#module-flask_login) with [Neo4j](https://neo4j.com/) graph database_ using the [py2neo](https://pypi.org/project/py2neo/) library


## Getting Started

The quickest way to run this script locally is by using [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/):

```shell
$ git clone git@github.com:taiwotman/flasklogin_neo4j.git
$ cd flasklogin-neo4j
$ pipenv shell
$ pipenv update
$ pip --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org install -r  requirements.txt 
$ flask run
```

## Assumptions
1. Prior knowledge of Neo4j Graph Database

2. The database is stored in the Neo4j import directory.

3. For test purpose, a dashboard for Patient Survey is provided, with empty data(please modify code to suite your usecase)

## References
Birchard, T.(2019), “Using Flask-Login to Handle User Accounts”. Retrieved from https://hackersandslackers.com/flask-login-user-authentication, and GITHUB:https://github.com/toddbirchard/flasklogin-tutorial

White, N.(2015), “Building a Python web application using Flask and Neo4j” OSCON, Portland, Oregon, Accessed at https://conferences.oreilly.com/oscon/open-source-2015/public/schedule/detail/42146
