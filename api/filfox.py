import requests

url = "https://filfox.info/api/v1"

payload = {}
headers = {}


import requests
import math

url = "https://filfox.info/api/v1"

payload = {}
headers = {}


def getMInerReward(miner_id):
    count = getMinerRewardCount(miner_id)
    page = math.ceil(count / 50)
    blocks = []
    for i in range(0, page):
        path = '/address/' + miner_id + '/blocks?pageSize=' + str(50) + '&page=' + str(i)
        response = requests.request("GET", url + path, headers=headers, data=payload)
        blocks.extend(response.json()['blocks'])
    return blocks


def getMinerRewardCount(miner_id):
    path = '/address/' + miner_id + '/blocks'
    response = requests.request("GET", url + path, headers=headers, data=payload)
    return response.json()['totalCount']
