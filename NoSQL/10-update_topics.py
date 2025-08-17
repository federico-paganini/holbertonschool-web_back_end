#!/usr/bin/env python3
"""
Module: update_topics_module
----------------------------
This module provides a function to update the 'topics' field of all documents
with a specific name in a MongoDB collection using PyMongo.

Function:
    update_topics(mongo_collection, name, topics)
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all documents in the collection that match the given name by
    setting the 'topics' field to the provided list.

    Args:
        mongo_collection (pymongo.collection.Collection)
        name (str): The name value used to filter documents to update.
        topics (list): A list of topics to set in the 'topics' field.
    """
    mongo_collection.update_many(
            { "name": name },
            { "$set": { "topics": topics } }
    )
