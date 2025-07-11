#!/usr/bin/env bash

readonly docker_user="cinnamoon"
readonly docker_image="fastapimongopipe"
readonly docker_tag="latest"

echo "STOPPING OLD VERSION..."
docker compose -f compose.deploy.yaml down -t 1
echo "DONE"

echo "PULLING NEW IMAGE..."
docker pull ${docker_user}/${docker_image}:${docker_tag}
echo "DONE"

echo "STARTING NEW VERSION..."
docker compose -f compose.deploy.yaml up --build -d
echo "DONE"