#!/usr/bin/env python3
"""
Contains a function to find specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Finds and returns the list of school having a specific topic.
    """
    schools = mongo_collection.find(
                {"topics": {"$all": [topic]}}
            )
    return schools
