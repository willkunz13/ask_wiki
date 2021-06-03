import requests
import pdb

url = 'http://localhost:8080/search'
query = 'What is Wosskow?'

response = requests.post(url, data=query)
pdb.set_trace()
print(0)
