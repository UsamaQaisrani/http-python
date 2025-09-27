from enum import Enum
from dataclasses import dataclass, field

class MessageType(Enum):
    REQUEST = "request"
    RESPONSE = "response"

class RequestType(Enum):
    GET = "get"
    POST = "post"
    HEAD = "head"
    PUT = "put"
    DELETE = "delete"

@dataclass
class Message:
    type : MessageType
    header: dict = field(default_factory=dict)
    body: dict = field(default_factory=dict)

    @classmethod
    def Request(cls, header=None, body=None):
        return cls(type=MessageType.REQUEST,
                header=header or {},
                body=body or {})

    @classmethod
    def Response(cls, header=None, body=None):
        return cls(type=MessageType.RESPONSE,
                header=header or {},
                body=body or {})
