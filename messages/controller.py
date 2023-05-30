import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(APP_DIR)

from typing import Union

from fastapi import Body, FastAPI, Response, status
from pydantic import BaseModel

import requests
import json
import uuid

from service import get_messages

app = FastAPI()


@app.get("/")
def get_message():
    return get_messages()
