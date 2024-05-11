How to run : 
step1 : install python
step 2 : install Django by 
```python
python -m pip install django
```
step 3 :startproject by
```python
django-admin startproject [Project_name]
Example - django-admin startproject monthly_challenges
or
py -m django startproject Yourprojectname
Eg->py -m django startproject mysite
```
step 4 : Creating apps (One project consisted of many apps) 
```python
django-admin manage.py startapp [app_name]
Example - django-admin manage.py startapp challenges
or
py -m django startapp Yourprojectname
Eg->py -m django startapp mysite
```
step 5 : Run the server
```python
python manage.py runserver
```
step 6 : make migrations.
Migratins are a feature which basically defines steps for Django to execute steps that which touch the DB and manipulate it.
```python
python manage.py makemigrations 
# this command will read the models present in the models.py
# file inside the app and will create code in migrations folder
# inside app to build tables in DB.
```
step 7 : To Create actual DB in sqlite : 
```python
python [manage.py](http://manage.py) migrate
# This command will create DB inside sqlite by reading contents
# present in migrations folder
```

NOTE : 
Last Module which is about Deployment is not completed because of AWS error.
