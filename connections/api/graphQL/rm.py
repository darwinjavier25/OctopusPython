import json
import requests

class getJson:

    def __init__(self, source):
        self.source = source
    
    def getData(self, url, query):
        params = {"query" : query}
        response = requests.get(url, params=params)
        print(self.source)
        return response
