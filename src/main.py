"""
This script is used to run our FastAPI web app. It uses SpaCy to tokenize \
content sent to our web app, and returning the entities in the requests.

Author: Jacques Thibodeau Date: 26/Jul/2021
"""

from typing import List
from fastapi import FastAPI
import spacy

from .models import Payload, Entities

app = FastAPI()

nlp = spacy.load("en_core_web_sm")
# doc = nlp("Apple is looking at buying U.K. startup for 1$ billion.")


@app.post("/ner-service")
async def get_ner(payload: Payload):
    """
    Receives a post request of a list of content and outputs a \
    list of entities for every request made. Since the function is \
    asynchronous, it can receive multiple requests at the same time and \
    output the entities for each request seperately.

    :param payload: A list of content
    """
    tokenize_content: List[spacy.tokens.doc.Doc] = [
        nlp(content.content) for content in payload.data
    ]
    document_entities = []
    for doc in tokenize_content:
        document_entities.append(
            [{"text": ent.text, "entity_type": ent.label_} for ent in doc.ents]
        )
    return [
        Entities(post_url=post.post_url, entities=ents)
        for post, ents in zip(payload.data, document_entities)
    ]
