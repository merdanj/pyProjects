#Author: Merdan Jumanov
#Date: 25/05/18
#Purpose: REST API and github gist

import requests
import json

BASE_URL = 'https://api.github.com'
LINK_URL = 'https://gist.github.com'
#DON'T FORGET TO REMOVE BEFORE PUSHING
username = '' #Github username
#THIS TOO
api_token = '' #Github token
gist_id = ''
header = {'X-Github-Username':'%s' % username,
          'Content-Type': 'application/json',
          'Authorization': 'token %s' % api_token}

url = "/gists"
data = {
    "description": "The description for this gist",
    "public": True,
    "files": {
        "file1.txt":{
            "content": "String file contents"
        }
    }
}

r = requests.post('%s%s' % (BASE_URL, url),
    headers=header,
    data=json.dumps(data))
print (r.json()['url'])

