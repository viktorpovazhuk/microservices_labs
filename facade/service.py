import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(APP_DIR)

from model.message import LoggingMessage, MessageDTO
from fastapi import status
import requests

LOGGING_URL = "http://localhost:8001/"
MESSAGES_URL = "http://localhost:8002/"

def post_message_log(msg_text: str):
    log_msg = LoggingMessage(msg_text)
    log_response = requests.post(LOGGING_URL, json=log_msg.__dict__)
    status_code = log_response.status_code
    return status_code

def get_messages_services():
    try:
        log_response = requests.get(LOGGING_URL)
    except:
        raise Exception(500)
    if log_response.status_code != status.HTTP_200_OK:
        raise Exception(log_response.status_code)
    try:
        msgs_response = requests.get(MESSAGES_URL)
    except:
        raise Exception(500)
    if msgs_response.status_code != status.HTTP_200_OK:
        raise Exception(msgs_response.status_code)
    messages = log_response.text.strip(
        "\"") + " : " + msgs_response.text.strip("\"")
    return messages