## Create a proof of concept of an infrastructure REST-API

Since you are a Python Software Engineer your team asks you to build a POC. You need to create and run an infrastructure application that provides information about the host where the application is running.

To achieve this, your team suggests you the following:
- Create a new folder in `~/infra-api-rest`.
- Create a new python venv in `~/infra-api-rest/venv`.
- Use the Flask framework https://flask.palletsprojects.com/en/3.0.x/quickstart/
- Create two endpoints to:
  - Get the uptime of the application 
  - Get the information about the host OS
- Test the application with the `curl` command:
  - curl localhost:$PORT/
  - curl localhost:$PORT/host-os

### Endpoints

**Get uptime**

Endpoint: `/`
HTTP method `GET`
Description: Retrieves the uptime in seconds of the REST API.
Success Response:

```
{
  "uptime": 102022
}
```

**Get host OS information**

Endpoint: `/host-os`
HTTP method `GET`
Description: Retrieves information about the host OS: type, version and host timezone.
Success Response:

```
{
  "typeOS": "Darwin",
  "versionOS": "23.0.0",
  "timezones": ["CET", "CEST"],
}
```


## Enhance the infrastructure app to report the status of other services

The application now needs to report the status of some critical services, like Bitbucket and Azure Pipelines services.

To achieve this, your team suggests you to create one endpoint `/health-services` to retrieve the health of the services.

To get the health of the services you can get the information from the following sources:
- https://bitbucket.status.atlassian.com/api#status
- https://learn.microsoft.com/en-us/rest/api/azure/devops/status/health/get?view=azure-devops-rest-7.1&tabs=HTTP#get-service-health-for-one-or-more-geographies

You can make use of [requests](https://requests.readthedocs.io/en/latest/) library to perform the HTTP request.

### Endpoints

**Get uptime**

Endpoint: `/health-services`
HTTP method `GET`
Description: Retrieves the health of github and Azure pipelines in Europe (EU).
Success Response:

```
{
  "bitbucket": "healthy",
  "azure-pipelines": "healthy",
}
```

## Improve the status page to store the health information in cache

Your team realizes that the endpoints to get the health information have a [Rate Limit](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/). That could impact the reliability of your application.

To guarantee that the information is always available your team suggests you the following:
- Use a new MySQL database in a container to store the information:
  - Database name: infra_app
  - Database user: infrauser
  - Database pwd: mylittlesecret
- Create a new table with the following fields:
  - id as Integer
  - status_bitbucket as varchar
  - status_azure_pipeline as varchar
  - last_update as datetime
- Store the status of the services in the table with the following logic:
  1. Get the latest record of the table.
  2. If the latest record is younger than 5 minutes then return the information of that record.
  3. If the latest record is older than 5 minutes then:
    1. Request the health information of the endpoints
    2. Add a new record in the table with the information.
- Create the database and table with the following code:

```SQL
CREATE DATABASE infra_app;
USE infra_app;
CREATE TABLE infra_status (
    id INT PRIMARY KEY AUTO_INCREMENT,
    status_bitbucket VARCHAR(255),
    status_azure_pipeline VARCHAR(255),
    last_update DATETIME
);
```

Insert in MYSQL with python https://www.w3schools.com/python/python_mysql_insert.asp
Select in MYSQL with python https://www.w3schools.com/python/python_mysql_insert.asp

## Set configurations via environment variables and add proper logging

The application should be able to be configured with the following environment variables:

- APP_PORT. Configure the listening port
- DB_HOST. Host of the database server
- DB_NAME. Name of the database
- DB_USER. Username to access to the database
- DB_PASSWORD. Password assigned to username of the database
- LOG_LEVEL. The level of severity of the events to track: DEBUG, INFO, WARNING, ERROR, CRITICAL

The environment variables should be defined with an `.env` file and loaded by the application.
You can make use of the package [python-dotenv](https://pypi.org/project/python-dotenv/).

The logging should be configured by using the [logging package](https://docs.python.org/3/howto/logging.html).

## Containerize the application

Create the Dockerfile and docker-compose.yaml files to run the application. The compose file should also contain the definition for the database server.