from uritemplate import URITemplate
import requests


t = URITemplate(
    'https://w3schools.com/python/demopage.htm{/gist_id}'
)
uri = t.expand(gist_id='20986')
print(uri)
resp = requests.get(uri)
print(resp.text)