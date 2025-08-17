#!/usr/bin/env python3
"""
Module: list_all_documents
--------------------------
This module provides a function to list all documents from
a MongoDB collection using pymongo.

Function:
    list_all(mongo_collection) -> list
"""


def list_all(mongo_collection) -> list:
    """
    Retrieve all documents from a given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo
        Collection object from which to fetch all documents.

    Returns:
        list: A list of dictionaries, each representing a
        document in the collection.
        
        Returns an empty list if the collection has no documents.
    """
    return list(mongo_collection.find())
