#!/usr/bin/env python3
"""
Module: insert_school_module
----------------------------
This module provides a function to insert a document into a MongoDB collection
using PyMongo and return the ObjectId of the inserted document.

Function:
    insert_school(mongo_collection, **kwargs) -> str
"""


def insert_school(mongo_collection, **kwargs) -> str:
    """
    Insert a document into the given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo
        Collection object where the document will be inserted.
        **kwargs: Arbitrary key-value pairs representing
        the fields of the document.

    Returns:
        str: The ObjectId of the inserted document as a string.
    """
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)
