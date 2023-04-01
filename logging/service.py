import mem_repository
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(APP_DIR)

from model.message import LoggingMessage


def log_message(msg_dto):
    msg = LoggingMessage.from_msg_dto(msg_dto)
    mem_repository.add(msg)


def get_messages():
    messages = mem_repository.get_all()
    return messages
