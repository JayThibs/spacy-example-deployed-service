from typing import List  # enforce List type from request
from pydantic import BaseModel  # enforce typing


class Content(BaseModel):
    post_url: str  # posted url needs to be string
    content: str  # received content needs to be string


class Payload(BaseModel):
    data: List[Content]  # received data needs to be list of Content


class SingleEntity(BaseModel):
    text: str
    entity_type: str


class Entities(BaseModel):
    post_url: str
    entities: List[SingleEntity]
