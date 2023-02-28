from typing import Union

from fastapi import Body, FastAPI, Response, status
from pydantic import BaseModel

import requests
import json
import uuid

app = FastAPI()

LOGGING_URL = "http://localhost:8001/"
MESSAGES_URL = "http://localhost:8002/"

class AcceptedMessage(BaseModel):
    text: str

class LoggingMessage:
    def __init__(self, uuid, text):
        self.uuid = uuid
        self.text = text

@app.post("/")
def accept_message(accept_msg: AcceptedMessage, response: Response):
    log_msg = LoggingMessage(str(uuid.uuid4()), accept_msg.text)
    log_response = requests.post(LOGGING_URL , json=log_msg.__dict__)
    response.status_code = log_response.status_code
    return ""

@app.get("/")
def get_messages(response: Response):
    log_response = requests.get(LOGGING_URL)
    if log_response.status_code != status.HTTP_200_OK:
        response.status_code = log_response.status_code
        return ""
    msgs_response = requests.get(MESSAGES_URL)
    if msgs_response.status_code != status.HTTP_200_OK:
        response.status_code = msgs_response.status_code
        return ""
    messages = log_response.text.strip("\"") + " : " + msgs_response.text.strip("\"")
    return messages