from typing import List  # enforce List type from request
from pydantic import BaseModel  # enforce typing


class Content(BaseModel):
    post_url: str  # posted url needs to be string
    content: str  # received content needs to be string


class Payload(BaseModel):
    data: List[Content]  # received data needs to be list of Content
