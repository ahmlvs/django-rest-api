# django-rest-api

## baseapi

1. create venv in terminal
```
python3 -m venv ~/.venvs/django-rest-api
source ~/.venvs/django-rest-api/bin/activate
```

2. install python or check it
```
python3 --version
```

3. install libraries
```
pip install django djangorestframework
pip freeze > requirements.txt
```

or requirements
```
pip install -r requirements.txt
```

4. use django to start a project with name "baseapi"
```
django-admin startproject baseapi
```

5. create api inside baseapi project
```
cd baseapi
python3 manage.py startapp api
```

6. add api in INSTALLED_APPS in setting.py
```
"rest_framework",
"api",
```

7. after can start create models, url, etc.

------

we will create simple api for users creation, update and delete.

1. define User in api/models

2. create db from our models
```
python3 manage.py makemigrations
python3 manage.py migrate
```

3. create serializer that transform model to json data in api

4. create views for api

5. add views to api/urls

6. add api/urls to baseapi/urls

7. start server
```
python3 manage.py runserver
```
