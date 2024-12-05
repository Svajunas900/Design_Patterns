"""Create class RateFacade - with implementation of returning 3 different JSON objects """
import json

"""Create separate json objects"""


class JsonObjectOne:
    def __init__(self):
        self.json_object = json.dumps({"Object_One": "Data"})

    def __str__(self):
        return self.json_object


class JsonObjectTwo:
    def __init__(self):
        self.json_object = json.dumps({"Object_Two": "Data"})

    def __str__(self):
        return self.json_object


class JsonObjectThree:
    def __init__(self):
        self.json_object = json.dumps({"Object_Three": "Data"})

    def __str__(self):
        return self.json_object

"""Facade method design combines classes into one Facade
Which makes easier to work with a lot of classes from one place"""


class RateFacade:
    def __init__(self):
        self.object_one = JsonObjectOne()
        self.object_two = JsonObjectTwo()
        self.object_three = JsonObjectThree()

    """ Return three json objects"""
    def display(self):
        return self.object_one, self.object_two, self.object_three


facade = RateFacade()
facade.display()
