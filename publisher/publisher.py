#!/usr/bin/env python
import os
import pika

amqp_url = os.environ['AMQP_URL']
print('URL: %s' % (amqp_url,))
parameters = pika.URLParameters(amqp_url)
print(parameters)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()