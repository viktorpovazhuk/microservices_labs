from uuid import uuid4 as gen_uuid
from pydantic import BaseModel


class MessageDTO(BaseModel):
    uuid: str = None
    text: str


class Message:
    def __init__(self, text: str, uuid=None):
        if uuid is None:
            self.uuid = str(gen_uuid())
        else:
            self.uuid = uuid
        self.text = text

    @classmethod
    def from_msg_dto(cls, msg_dto):
        return cls(msg_dto.text, msg_dto.uuid)
