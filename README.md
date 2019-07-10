# crawler
Flask Application



for run create virtualenv with python 3.6 :
```
$ virtualenv -p python3.6 venv
```

Run this commands:
```
$ export FLASK_APP=micro.py

$ export FLASK_ENV=development
```


Run this commands for create database:
```
$ flask db init

$ flask db migrate

$ flask db upgrade
```

and for running application should run :

```
$ flask run
```