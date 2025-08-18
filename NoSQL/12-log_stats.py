#!/usr/bin/env python3
"""
This module connects to a MongoDB database and analyzes the 'nginx' logs collection.
It provides a summary of the total number of log entries, a breakdown of requests
by HTTP method (GET, POST, PUT, PATCH, DELETE), and counts how many GET requests
were made specifically to the '/status' endpoint.ls
"""
from pymongo import MongoClient


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
