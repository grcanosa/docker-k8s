# Run a postgresql database


docker run  -p 5432:5432 -e POSTGRES_PASSWORD=datahack -e POSTGRES_USER=datahack -e POSTGRES_DB=datahack  postgres:14