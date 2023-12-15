import json
import requests 
import configparser
from rm import getJson
import pandas as pd 

#params = {"query": graphql_query}
#response = requests.get(request_url, params=params)
#data = response.json()
#print(data)

config = configparser.ConfigParser()
config.read('/home/dw/Octopus/PythonOctopus/resources/config.ini')
query1 = config['paths']['query']
url1 = config['paths']['url']

inst = getJson
a = inst.getData(url1, query1)
print(a.json())

data = a.json()

df = pd.DataFrame(data['data']['characters']['results'])
print(df)