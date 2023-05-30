import os
import sys

import mem_repository as repository
from aiokafka import AIOKafkaConsumer
import asyncio

from model.message import Message


async def subscribe_kafka_mq(consumer):
    async for msg in consumer:
        text = msg.value.decode("utf-8")
        uuid = msg.key.decode("utf-8")
        msg = Message(text, uuid)
        repository.add(msg)
        print({"uuid": msg.uuid, "text": msg.text})


async def start_message_consumer():
    consumer = AIOKafkaConsumer(
        "messages",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
    )
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        await subscribe_kafka_mq(consumer)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


asyncio.create_task(start_message_consumer())


def get_messages():
    messages = repository.get_all()
    return messages
