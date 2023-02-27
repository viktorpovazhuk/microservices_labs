from typing import Union

from fastapi import Body, FastAPI, Response, status
from pydantic import BaseModel

import requests
import json
import uuid

app = FastAPI()

LOGGING_URL = "http://localhost:8001/"

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