import re
import requests
import json

endpoint = "http://127.0.0.1:5000/url"


def post_data(url, desc):
    payload = json.dumps(
        {
            "url": url,
            "desc": desc
        }
    )
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", endpoint, headers=headers, data=payload)
    print(response.text)


def read_file(filename):
    num_lines = 0
    with open(filename) as file:
        num_lines = sum(1 for line in file)
        file.seek(0)
        while num_lines > 0:
            url = file.readline().rstrip()
            desc = file.readline().rstrip()
            desc = re.sub('[^A-Za-z0-9\s]+', '', desc)
            desc = re.sub('[\s]+', ' ', desc)
            num_lines = num_lines - 2
            print("{0} Payload: {{url: {1}, desc: {2}}}".format(num_lines, url, desc))
            # r = requests.post('http://127.0.0.1:5000/url',
            #                   data={'url': url, 'desc': desc})
            post_data(url, desc)


read_file("data/bookmarks_1.html")
