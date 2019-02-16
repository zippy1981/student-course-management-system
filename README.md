# student-course-management-system

## Docker setup

1. run `docker-compose run web pipenv run python manage.py migrate`
2. run `docker-compose up`
3. navigate to http://localhost:8000 in your browser

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

Then connect to adminer on http://localuost:8080 or with any other sql client directly.