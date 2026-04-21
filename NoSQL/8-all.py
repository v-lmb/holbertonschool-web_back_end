#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    """
    function list_all
    """
    return list(mongo_collection.find())
