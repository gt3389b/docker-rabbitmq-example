#!/usr/bin/env python
import os
import pika

amqp_url = os.environ['AMQP_URL']
print(f'URL: {amqp_url}')
parameters = pika.URLParameters(amqp_url)
print(parameters)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello',
                      properties=pika.BasicProperties(
                            content_type='application/json',
                            message_id='42',
                            user_id='13',
                            correlation_id='666'),
                      body='{"payload": "Hello World!"}')
print(" [x] Sent 'Hello World!'")
connection.close()
