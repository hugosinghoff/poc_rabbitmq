#!/usr/bin/env python
import pika

#config
credentials = pika.PlainCredentials('user', 'bitnami')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=8050, credentials=credentials))
channel = connection.channel()

#publish messages
channel.queue_declare(queue='hello')
base = 'Hello World number '
nb_publish=3

for i in range(nb_publish):
    channel.basic_publish(exchange='', routing_key='hello', body= base + str(i))

#close connection
connection.close()
