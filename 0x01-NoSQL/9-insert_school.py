#!/usr/bin/env python3
"""
contains function to insert a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection.
    Retruns the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
