"""
This script creates the BaseModel classes so that we can enforce typing for \
requests to our app.

Author: Jacques Thibodeau
Date: 26/Jul/2021
"""

from typing import List  # enforce List type from request
from pydantic import BaseModel  # enforce typing


class Content(BaseModel):  # pylint: disable=too-few-public-methods
    """This class makes sure the posted content is a string."""

    post_url: str  # posted url needs to be string
    content: str  # received content needs to be string


class Payload(BaseModel):  # pylint: disable=too-few-public-methods:
    """This class makes sure the content has been placed in a list."""

    data: List[Content]  # received data needs to be list of Content


class SingleEntity(BaseModel):  # pylint: disable=too-few-public-methods
    """This class makes sure the output is a single entity string."""

    text: str
    entity_type: str


class Entities(BaseModel):  # pylint: disable=too-few-public-methods
    """This class makes sure the output is a list of entities."""

    post_url: str
    entities: List[SingleEntity]
