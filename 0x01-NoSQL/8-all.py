#!/usr/bin/env python3
"""
script to all documents in a MongoDB collection
"""


def list_all(mongo_collection):
    """
    Function that returns a collection of documents in a collection otherwise
    empty list.
    """
    if mongo_collection is None:
        return []

    return mongo_collection.find()
