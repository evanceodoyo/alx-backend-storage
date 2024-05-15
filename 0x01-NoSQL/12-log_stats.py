#!/usr/bin/env python3
"""
Module to prints Nginx logs in a MongoDB
"""
from pymongo import MongoClient


def print_nginx_stats(mongo_collection):
    """
    Function to provide stats about Nginx logs stored in MongoDB.
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    num_logs = mongo_collection.count_documents({})
    num_status_check = len(list(mongo_collection.find(
                {"method": "GET", "path": "/status"}
            )))

    print("{} logs".format(num_logs))
    print("Methods:")
    for method in methods:
        count = len(list(mongo_collection.find({"method": method})))
        print("\tmethod {}: {}".format(method, count))
    print("{} status check".format(num_status_check))


def run():
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    print_nginx_stats(nginx_collection)


if __name__ == "__main__":
    """Driver function"""
    run()
