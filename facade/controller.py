import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(APP_DIR)

from service import post_message_log, post_message, get_messages_services
from model.message import MessageDTO
from fastapi import Body, FastAPI, Response, status
import requests
import json


app = FastAPI()


@app.post("/")
def accept_message(accepted_msg: MessageDTO, response: Response):
    response.status_code = post_message(accepted_msg.text)
    return ""


@app.get("/")
def give_messages(response: Response):
    messages = ""
    try:
        messages = get_messages_services()
    except Exception as ex:
        response.status_code = int(str(ex))
    return messages
