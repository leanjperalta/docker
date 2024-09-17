# Docker Configuration Files

This repository contains Docker configuration files, including docker-compose.yml files for different services. These files allow you to quickly set up and run containers for various services on your local machine or server.
Getting Started

To use the configuration files in this repository, follow these steps:

## 1. Clone the Repository

First, clone the repository to your local machine using the following command:
```
bash
git clone https://github.com/leanjperalta/docker.git
``

## 2. Navigate to the Desired Service

Each service has its own directory containing the relevant docker-compose.yml file. Navigate to the service you're interested in, for example:

bash

cd docker/service-name

## 3. Run Docker Compose

To spin up the containers for the chosen service, use Docker Compose:
```
bash
docker-compose up -d
``
This command will start the service in detached mode, running in the background.

## 4. Stopping the Services

To stop the services and remove the containers, networks, and volumes created by Docker Compose, run:
```
bash
docker-compose down
``

### Prerequisites

Make sure you have the following installed on your machine:

    **Docker**
    **Docker Compose**

### Available Services

The repository contains configuration files for the following services:

    **Service 1: Traefik**
    **Service 2: Semaphore (current & legacy)**
    **Service 3: Jenkins**
    **Service 4: Homepage**

### Contributing

Feel free to submit issues or pull requests if you'd like to contribute to this repository. Make sure to follow the contribution guidelines.
License

***This repository is licensed under the MIT License. See the LICENSE file for more details.***
