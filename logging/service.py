import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(APP_DIR)

from model.message import LoggingMessage
import hazelcast_repository


def log_message(msg_dto):
    msg = LoggingMessage.from_msg_dto(msg_dto)
    hazelcast_repository.add(msg)


def get_messages():
    messages = hazelcast_repository.get_all()
    return messages

