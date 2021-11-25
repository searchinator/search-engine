import requests

url = 'http://192.168.254.20:5000'
search_endpoint = '/search'
url_endpoint = '/url'

# Populates the MongoDB database with a sample URL.
# This is commented out as this should be performed only once.
'''
requests.post(url=url + url_endpoint, json={
    'url': 'https://github.com/searchinator/search-engine/',
    'desc': 'Searchinator search engine',
})
'''

# Requests to find the sample URL made before.
r = requests.post(url=url + search_endpoint + '?query=Searchinator search engine', json={
    'page_size': 10,
    'page_num': 1,
})

# Outputs the result from the server.
print(r.json())
