from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel

import requests
import uuid

app = FastAPI()

messages = {}

class LoggingMessage(BaseModel):
    uuid: str
    text: str

@app.post("/")
def accept_message(msg: LoggingMessage):
    messages[msg.uuid] = msg.text
    print({"uuid": msg.uuid, "text": msg.text})
    return ""