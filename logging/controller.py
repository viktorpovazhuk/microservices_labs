from service import log_message, get_messages
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(APP_DIR)


from model.message import LoggingMessage, MessageDTO
from fastapi import Body, FastAPI


app = FastAPI()


@app.post("/")
def accept_message(msg_dto: MessageDTO):
    print({"uuid": msg_dto.uuid, "text": msg_dto.text})
    log_message(msg_dto)
    return ""


@app.get("/")
def give_messages():
    messages = get_messages()
    return messages
