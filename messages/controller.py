from typing import Union

from fastapi import Body, FastAPI, Response, status
from pydantic import BaseModel

import requests
import json
import uuid

app = FastAPI()

@app.get("/")
def get_message():
    return "not implemented yet"