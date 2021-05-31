from typing import List
from pydantic import BaseModel


class Content(BaseModel):
    post_url: str
    content: str


class Payload(BaseModel):
    data: List[Content]
