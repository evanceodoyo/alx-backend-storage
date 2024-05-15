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


def print_top_ips(mongo_collection):
    """
    Print the top 10 of the most present IPs in a collection.
    """
    results = mongo_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    print("IPs:")
    for res in results:
        ip = res['_id']
        requests_count = res['totalRequests']
        print('\t{}: {}'.format(ip, requests_count))


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    print_nginx_stats(client.logs.nginx)
    print_top_ips(client.logs.nginx)
