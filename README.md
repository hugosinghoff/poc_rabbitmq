# POC Rabbitmq

## Install

`pip install pika`

## Docker image used

`https://hub.docker.com/r/bitnami/rabbitmq`

## RabbitMQ tutorial

This POC used the python language and an WSL2(ubuntu) environement, others language are available :

`https://www.rabbitmq.com/tutorials/tutorial-one-python.html`

## Credentials of the docker image

`id : user`
`password : bitnami`

# Config and data

You can configure the data and config with the docker-compose file.
You might have to give rights to the folders :

`sudo chown -R 1001:1001 $RABBITMQ_VOLUMES`
with `export RABBITMQ_VOLUMES="~/poc_rabbitmq"`
