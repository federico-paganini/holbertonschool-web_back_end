#!/usr/bin/env python3
from pymongo import MongoClient
"""
Script to count documents in nginx logs collection and show breakdown by HTTP method.
"""


if __name__ == "__main__":
    """Checks all elements in a pymongo collection"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    print(f"{nginx_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")

    check_get = nginx_collection.count_documents(
        {'method': 'GET', 'path': "/status"})
    print(f"{check_get} status check")
