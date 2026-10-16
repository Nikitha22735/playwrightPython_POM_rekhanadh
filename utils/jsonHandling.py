
import json


def jsonHandling(path):
    with open(path) as data:
        formattedData = json.load(data)
        return formattedData