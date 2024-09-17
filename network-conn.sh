#!/bin/bash

# Get the list of all networks
networks=$(docker network ls --format "{{.Name}}")

# Loop through each network and list connected containers
for network in $networks; do
  echo "Network: $network"
  containers=$(docker network inspect --format "{{range .Containers}}{{.Name}} {{end}}" $network)
  if [ -z "$containers" ]; then
    echo "  No containers connected"
  else
    for container in $containers; do
      echo "  Container: $container"
    done
  fi
  echo
done

