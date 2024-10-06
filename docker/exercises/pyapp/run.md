docker network create datahack-test
docker volume create datahack-db
docker run --name=datahack-db --network datahack-test -p 5432:5432 -e POSTGRES_PASSWORD=datahack -e POSTGRES_USER=datahack -e POSTGRES_DB=datahack -v datahack-db:/var/lib/postgresql/data/  postgres:14
docker build -t datahack-app .

docker run --rm --name datahack-app --network datahack-test -e DB_USER=datahack -e DB_PASSWORD=datahack -e DB_HOST=datahack-db -e DB_PORT=5432 -e DB_NAME=datahack -p 5000:5000 datahack-app .