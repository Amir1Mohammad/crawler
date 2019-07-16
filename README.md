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

for run in another port you can :
```
$ flask run --host=0.0.0.0 --port=8080
```

first should be run redis on docker with this command :
```
$ sudo docker-compose up -d redis
```

for run celery :
```
$ celery worker -A controller.celery --loglevel=info
```