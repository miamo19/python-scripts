import http
import json
from urllib.request import urlopen
import ipinfo as ipinfo

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.loads(response.read())

print(data)
