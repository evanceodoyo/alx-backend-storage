#!/usr/bin/env python3
"""
Contains a function to change all topics of a document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a document based on the name.

    Args:
        mongo_collection: pymongo collection object
        name (string): will be the school name to update
        topics (list of strings): list of topics approached in the school
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"name": f"{name} {topics}"}}
            )
