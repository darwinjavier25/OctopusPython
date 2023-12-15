import json
import requests

class getJson:
    
    def getData(url, query):
        params = {"query" : query}
        response = requests.get(url, params=params)
        return response
