#!/bin/bash

docker compose --profile test up -d
docker compose logs -f test
docker compose down
