# Django React Boilerplate

[![alt text](https://github.com/justdjango/django-react-boilerplate/blob/master/thumbnail.png "Logo")](https://youtu.be/YKYVv0gm_0o)

This repository contains a boilerplate project setup for Django and React. The project contains backend user authentication with the Django Rest Framework and rest-auth. The frontend has react redux setup for user authentication by storing the token in localstorage.

[Watch the tutorial on how to integrate Django and React](https://youtu.be/YKYVv0gm_0o)

## Backend development workflow

```json
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Frontend development workflow

```json
npm i
npm start
```

## For deploying

```json
npm run build
```
