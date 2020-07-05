#!/usr/bin/env python
import os
import pika
import time

amqp_url = os.environ['AMQP_URL']
print(f'URL: {amqp_url}')
parameters = pika.URLParameters(amqp_url)
print(parameters)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

# user_id='guest',
while(1):
    channel.basic_publish(exchange='', routing_key='hello',
                        properties=pika.BasicProperties(
                                content_type='application/json',
                                message_id='42',
                                correlation_id='666'),
                        body='{"payload": "Hello World!"}')
    print(" [x] Sent 'Hello World!'")
    time.sleep(10)
connection.close()
time.sleep(10)
