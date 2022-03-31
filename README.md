## flasklogin_neo4j
_This framework is an implementation of the [Flask Login](https://flask-login.readthedocs.io/en/latest/#module-flask_login) with [Neo4j](https://neo4j.com/) graph database_ using the [py2neo](https://pypi.org/project/py2neo/) library.

<p align="center"> 
 <img width="600" height="400" src="https://github.com/taiwotman/flasklogin_neo4j/blob/master/application/static/dist/img/flasklogin_neo4j_framework.png"></p>

### Dependencies
![Python](https://img.shields.io/badge/Python-v3.7-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v1.1.1-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Login](https://img.shields.io/badge/Flask--Login-v0.4.1-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Assets](https://img.shields.io/badge/Flask--Assets-v0.12-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![WTForms](https://img.shields.io/badge/WTForms-v2.2.1-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Py2neo](https://img.shields.io/badge/Py2neo-v4.30-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Bokeh](https://img.shields.io/badge/Bokeh-v2.2.0-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)

### Project discussion
[Implementing Flask Login with Neo4j](https://medium.com/@taiwo.adetiloye/implementing-flask-login-with-neo4j-database-54a3ac0d4cdf).

### Getting Started

To get started quickly use [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/):

```shell
$ git clone git@github.com:taiwotman/flasklogin_neo4j.git
$ cd flasklogin-neo4j
$ pipenv shell
$ pipenv update
$ pip install -r  requirements.txt 
$ flask run
```

### Basic assumptions
1. Prior knowledge of  Neo4j  cypher queries and graph database.

2. The Neo4j server is started and the database is stored in the Neo4j import directory.

3. For test purpose,  sentiment analytics dashboard is provided  without the data. You will need to modify the source code to fit your usecase.

4. [Bokeh](https://pypi.org/project/bokeh/) is used to create the sentiment analytics dashboard.

### References
Birchard, T.(2019), “Using Flask-Login to Handle User Accounts”. Retrieved from https://hackersandslackers.com/flask-login-user-authentication, and GITHUB: https://github.com/toddbirchard/flasklogin-tutorial.

White, N.(2015), “Building a Python web application using Flask and Neo4j” OSCON, Portland, Oregon, Accessed at https://conferences.oreilly.com/oscon/open-source-2015/public/schedule/detail/42146.

### Community contribution

If you are interested in contributing to improve this project; please, do either of the following:

* Open an [issue](https://github.com/taiwotman/flasklogin_neo4j/issues?q=is%3Aissue+is%3Aclosed)

* Fork repository

* Send me a [message](https://www.taiwotman.github.io)

