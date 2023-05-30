import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(APP_DIR)

from model.message import Message
import hazelcast_repository as repository


def log_message(msg_dto):
    msg = Message.from_msg_dto(msg_dto)
    repository.add(msg)


def get_messages():
    messages = repository.get_all()
    return messages
