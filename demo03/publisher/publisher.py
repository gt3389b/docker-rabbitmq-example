#!/usr/bin/env python
import os
import pika
import time
import asyncio
from aio_pika import connect_robust
from aio_pika.patterns import Master

amqp_url = os.environ['AMQP_URL']

async def main(loop):
    #connection = await connect_robust("amqp://guest:guest@127.0.0.1/")
    connection = await connect_robust(amqp_url, loop=loop)
    print("Connected")

    async with connection:
        # Creating channel
        channel = await connection.channel()
        print("Got channel")

        master = Master(channel)
        print("Got master")

        # Creates tasks by proxy object
        for task_id in range(10):
            await master.proxy.my_task_name(task_id=task_id)

        # Or using create_task method
        for task_id in range(10):
            print("Starting ",task_id)
            await master.create_task(
                "my_task_name", kwargs=dict(task_id=task_id)
            )

        while(1):
            time.sleep(1)

if __name__ == "__main__":
    time.sleep(15)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
