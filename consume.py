#!/usr/bin/env python
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

#config
credentials = pika.PlainCredentials('user', 'bitnami')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=8050, credentials=credentials))
channel = connection.channel()

#config consuming action
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

#start consuming
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
