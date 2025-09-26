#! /usr/bin/env sh

# Exit in case of error
set -e
set -x

docker compose -f docker/docker-compose.yml build
docker compose -f docker/docker-compose.yml down -v --remove-orphans # Remove possibly previous broken stacks left hanging after an error
docker compose -f docker/docker-compose.yml up -d
docker compose -f docker/docker-compose.yml exec -T backend bash scripts/tests-start.sh "$@"
docker compose -f docker/docker-compose.yml down -v --remove-orphans
