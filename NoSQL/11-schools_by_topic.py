#!/usr/bin/env python3
"""
Module: schools_by_topic
------------------------
Function to return all schools that have a given topic in their 'topics' list.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Find all documents in the collection where 'topics' contains the given topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        topic (str): The topic to search for.
    """
    result = mongo_collection.find(
        { "topics": topic }
    )

    return result
