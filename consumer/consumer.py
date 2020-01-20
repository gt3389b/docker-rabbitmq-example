#!/usr/bin/env python
import os
import pika
import time

amqp_url = os.environ['AMQP_URL']
print('URL: %s' % (amqp_url,))
parameters = pika.URLParameters(amqp_url)
print(parameters)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()