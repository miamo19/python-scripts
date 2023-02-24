import http
import json
from urllib.request import urlopen
import ipinfo as ipinfo

#Provide the url
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.loads(response.read())

print(data)
