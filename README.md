# djangobookstore

## Build for local host

```bash
# build
$ docker-compose build
$ docker-compose up
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


# Endpoints
```
http://localhost:8000/api/books/  [GET, POST]
http://localhost:8000/api/authors/ [GET, POST]

http://localhost:8000/api/books/{id}/ [PUT, DELETE]
http://localhost:8000/api/authors/{id}/ [PUT, DELETE]
```