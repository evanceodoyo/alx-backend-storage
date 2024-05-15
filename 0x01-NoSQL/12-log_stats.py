#!/usr/bin/env python3
"""
Module to prints Nginx logs in a MongoDB
"""
from pymongo import MongoClient


def method_counter(mongo_collection, method):
    "Counts the number of occurences of a given method in a collection."
    return mongo_collection.count_documents({"method": method})


def nginx_stats(mongo_collection):
    """
    Function to provide stats about Nginx logs stored in MongoDB.
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    num_logs = mongo_collection.count_documents({})
    num_status_check = mongo_collection.count_documents(
                {"method": "GET", "path": "/status"}
            )

    print("{} logs".format(num_logs))
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(
            method,
            method_counter(mongo_collection, method))
        )
    print("{} status check".format(num_status_check))


def run():
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    nginx_stats(nginx_collection)


if __name__ == "__main__":
    """Driver function"""
    run()
