# student-course-management-system

Student course catalog example DJango app.

## Notes about docker and pipenv

This project uses [pipenv](https://pipenv.readthedocs.io/en/latest/) inside its docker container to manage dependencies insted of manually using `virtualenv` and `pip` with `requirements.txt`.
To run a command inside the pipenv virtualenv locally, you must use the command `pipenv run command [args]`.
To run a command inside the **already running running** docker container, you must use the command `docker-compose exec web command [args]`.
Therefore, to run a command inside the pipenv, inside the **already running running** docker container, you must use the command `docker-compose exec web pipenv run command [args]`.

If you want to start a new container (e.g. if you don't have the web server running) to run a command just replace `docker-compose exec` with `docker-compose run`. Note that this will cause the db container to start up and remain running.

## Docker setup

1. run `docker-compose run web pipenv run python manage.py migrate`
2. run `docker-compose up -d` or to to keep a tail of the container console messages  in a new terminal omit the -d (i.e. `docker-compose up`)
3. run `docker-compose exec web pipenv run python manage.py loaddata initial_data.json`
4. run `docker-compose exec web pipenv run python manage.py createsuperuser` and enter auth information
5. navigate to <http://localhost:8000> in your browser

### Resetting the envinment

If you want to start with a clean databaase the quickest way is with the following commands:

1. `docker-compose rm -fvs db`
2. `docker-compose up -d db`
3. `docker-compose exec web pipenv run python manage.py migrate`
4. `docker-compose exec web pipenv run python manage.py loaddata initial_data.json`

### Connecting to the database for local devugging, etc

1. Create a docker-compose.override.yml with the following:

```yml
version: '3.4'

services:
  db:
    ports:
      - "5432:5432"
    #environment:
    #  POSTGRES_PASSWO: "stud3ntC0urse"
  adminer:
    image: adminer
    ports:
      - 8080:8080
```

Then connect to adminer on <http://localuost:8080> or with any other sql client directly. 