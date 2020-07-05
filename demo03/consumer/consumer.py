#!/usr/bin/env python
import os
import json
import pika
import time
import asyncio
from aio_pika import connect_robust
from aio_pika.patterns import Master, RejectMessage, NackMessage

amqp_url = os.environ['AMQP_URL']

async def worker(*, task_id):
    # If you want to reject message or send
    # nack you might raise special exception

    print("Working on: ",task_id)

    if task_id % 2 == 0:
        raise RejectMessage(requeue=False)

    if task_id % 2 == 1:
        raise NackMessage(requeue=False)


async def main(loop):
    #connection = await connect_robust("amqp://guest:guest@127.0.0.1/")
    #connection = await connect_robust("amqp://guest:guest@rabbitmq/")
    connection = await connect_robust(amqp_url, loop=loop)
    print("Connected")

    # Creating channel
    channel = await connection.channel()
    print("Got Channel")

    master = Master(channel)
    await master.create_worker("my_task_name", worker, auto_delete=True)
    print("Worker created")

    return connection


if __name__ == "__main__":
    time.sleep(10)
    loop = asyncio.get_event_loop()
    connection = loop.run_until_complete(main(loop))
    try:
        loop.run_forever()
    finally:
        loop.run_until_complete(connection.close())
