#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """
    function school_by_topic
    """
    return list(mongo_collection.find({"topics": topic}))
