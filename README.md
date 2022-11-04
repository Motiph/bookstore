# djangobookstore

## Build for local host

```
# build
$ docker-compose build
$ docker-compose up
```

```
# setup
$ docker-compose run django python manage.py makemigrations
$ docker-compose run django python manage.py migrate
# docker-compose run createsuperuser
```

# Using the data.json to pupulate models
```
# generate fake data
# docker-compose run django python manage.py generate_data
```


# Endpoints
```
http://localhost:8000/api/books/  [GET, POST]
http://localhost:8000/api/authors/ [GET, POST]

http://localhost:8000/api/books/{id}/ [PUT, DELETE]
http://localhost:8000/api/authors/{id}/ [PUT, DELETE]
```