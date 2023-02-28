from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel

import requests
import uuid

app = FastAPI()

MESSAGES_MAP = {}

class Message(BaseModel):
    uuid: str
    text: str

@app.post("/")
def save_message(msg: Message):
    MESSAGES_MAP[msg.uuid] = msg.text
    print({"uuid": msg.uuid, "text": msg.text})
    return ""

@app.get("/")
def get_messages():
    messages = str(list(MESSAGES_MAP.values()))
    return messages