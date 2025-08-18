#!/usr/bin/env python3

def schools_by_topic(mongo_collection, topic) -> list[dict]:
    result = mongo_collection.find(
        { "topics": topic }
    )

    return result
