# Pollster App (Django project)

> Python Django app to create polls with questions/choices

## Quick Start
``` bash
cd pollster-django-crash
# Install dependencies
pip install pipenv

pipenv shell
# Install django
pipenv install django

cd pollster
# Serve on localhost:8000
python manage.py runserver
```
##Adminstrator account:

http://127.0.0.1:8000/admin/
```
username: Karim
password: kr20520rim
```
###To create a poll: go to polls -> new poll. 
###To create a qestion: go to questions -> create new question -> sellect question type (Multi Choice Question, Single Choice Question, Short answer question), sellect the desired poll.
###To create choice: go to choices -> create new choice.
###To view responses: Go to Response

##User webpage:

http://127.0.0.1:8000/
