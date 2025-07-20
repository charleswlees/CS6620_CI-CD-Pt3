#!/bin/bash

docker-compose build --no-cache
docker-compose down -v
docker-compose up

