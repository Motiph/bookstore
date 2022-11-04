# djangobookstore

## Build for local host

```bash
# build
$ docker-compose build
```

# **Make a db.sqlite3 or setup settings.py file for another database**

```bash
# make a sqlite3 file
$ touch db.sqlite3
```

```bash
# setup
$ docker-compose run django python manage.py makemigrations
$ docker-compose run django python manage.py migrate
$ docker-compose run django python manage.py createsuperuser
```

# Testing
```bash
$ docker-compose run django python manage.py tests apps.core.tests
```

# Using the data.json to pupulate models
```bash
# generate fake data
$ docker-compose run django python manage.py generate_data
```

#Run
```bash
$ docker-compose up
```


# Endpoints
```
http://localhost:8000/api/books/  [GET, POST]
http://localhost:8000/api/authors/ [GET, POST]

http://localhost:8000/api/books/{id}/ [PUT, DELETE]
http://localhost:8000/api/authors/{id}/ [PUT, DELETE]
```
