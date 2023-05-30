import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(APP_DIR)

from model.message import Message, MessageDTO
from fastapi import status
import requests
import random
from kafka import KafkaProducer

LOGGING_URLS = [
    "http://localhost:8001/",
    "http://localhost:8002/",
    "http://localhost:8003/",
]
MESSAGES_URLS = [
    "http://localhost:8004/",
    "http://localhost:8005/",
]


def post_message(msg_text: str):
    msg = Message(msg_text)
    status_code = post_message_log(msg)
    if status_code != status.HTTP_200_OK:
        return status_code
    status_code = post_message_messages(msg)
    return status_code


def post_message_log(msg: Message):
    log_url = random.choice(LOGGING_URLS)
    log_response = requests.post(log_url, json=msg.__dict__)
    status_code = log_response.status_code
    return status_code


def post_message_messages(msg: Message):
    producer = connect_kafka_producer()
    publish_kafka_mq(producer, msg.uuid, msg.text)


def publish_kafka_mq(producer, key, value):
    try:
        key_bytes = bytes(key, encoding="utf-8")
        value_bytes = bytes(value, encoding="utf-8")
        producer.send("messages", key=key_bytes, value=value_bytes)
        producer.flush()
        print("Message published successfully.")
        return status.HTTP_200_OK
    except Exception as ex:
        print("Exception in publishing message")
        print(str(ex))


def connect_kafka_producer():
    producer = None
    try:
        producer = KafkaProducer(
            bootstrap_servers=["localhost:9092"], api_version=(0, 10)
        )
    except Exception as ex:
        print("Exception while connecting Kafka")
        print(str(ex))
    finally:
        return producer


def get_messages_services():
    log_url = random.choice(LOGGING_URLS)
    try:
        log_response = requests.get(log_url)
    except:
        raise Exception(500)
    if log_response.status_code != status.HTTP_200_OK:
        raise Exception(log_response.status_code)
    msg_url = random.choice(MESSAGES_URLS)
    try:
        msgs_response = requests.get(msg_url)
    except:
        raise Exception(500)
    if msgs_response.status_code != status.HTTP_200_OK:
        raise Exception(msgs_response.status_code)
    messages = log_response.text.strip('"') + " : " + msgs_response.text.strip('"')
    return messages
