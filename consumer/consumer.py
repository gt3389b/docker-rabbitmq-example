#!/usr/bin/env python
import os
import json
import pika
import time

amqp_url = os.environ['AMQP_URL']
print(f'URL: {amqp_url}')
parameters = pika.URLParameters(amqp_url)
print(parameters)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(channel, method, properties, body):
    print(f"channel {channel}")
    print(f"method {method}")
    print(f"properties {properties}")
    # print("properties {0}".format(dir(properties)))
    list_properties = \
        ('app_id', 'cluster_id', 'content_encoding', 'content_type',
         'correlation_id', 'decode', 'delivery_mode', 'encode',
         'expiration', 'headers', 'message_id', 'priority',
         'reply_to', 'timestamp', 'type', 'user_id')
    for k in list_properties:
        print("properties {0} : {1}".format(k, getattr(properties, k)))

    print(" [x] Received : {0}".format(str(json.loads(body))))


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()