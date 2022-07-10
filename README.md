# Sparkle
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/SiMDE-Projects/sparkle/master.svg)](https://results.pre-commit.ci/latest/github/SiMDE-Projects/sparkle/master)

Les calculs n'étaient pas bons Kevin !


## Requirements

- `docker`
- `yarn`

## Get started

1. Sparkle's project is containerized with Docker, so you can start and init the django app by creating a `docker-compose.override.yml` file at repository's root containing these values:
```Dockerfile
version: "3.9"
services:
  web:
    environment:
      GESASSO_OAUTH_SETTINGS_ID: YOUR-CLIENT-ID
      GESASSO_OAUTH_SETTINGS_SECRET: YOUR-CLIENT-SECRET
```

2. Then execute theses commands :

```bash
$ docker compose up -d # Start up the docker containers
$ docker compose run --rm web python manage.py migrate # Initialize database
$ docker compose run --rm web python manage.py createsuperuser --username sparkle --email sparkle@assos.utc.fr --skip-checks # Create a local superuser
```

3. You can start the dev environment with `yarn dev` and go to http://localhost:8000/front/

## Urls

Once the project is initialized, you can go to theses urls to work:

- `http://localhost:8000` for the api
- `http://localhost:8080` for adminer if docker is started with debug profile

## Code style check commands

Pull requests not complying with code repository's format and style rules would be marked as stall until fixed.

You can execute `black` and `flake8` with the 2 following commands to automatically lint/fix your code.
If you add/remove/update an API route, you can regenerate the OpenAPI documentation file with the third command.

- Code format `docker compose run --rm web black /code`
- Code style `docker compose run --rm web flake8 sparkle`
- Generate openApi file `docker compose run --rm web ./manage.py generateschema --file openapi-schema.yml`
