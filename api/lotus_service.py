import json

import requests

from api import URL


def state_miner_power(miner_id):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {'jsonrpc': "2.0",
               'method': "Filecoin.StateMinerPower",
               'params': [miner_id, None],
               'id': 3}
    # sending post request and saving the response as response object
    r = requests.get(url=URL, data=json.dumps(payload), headers=headers)
    return r.json()


def state_miner_info(miner_id):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {'jsonrpc': "2.0",
               'method': "Filecoin.StateMinerInfo",
               'params': [miner_id, None],
               'id': 3}
    # sending post request and saving the response as response object
    r = requests.get(url=URL, data=json.dumps(payload), headers=headers)
    return r.json()


def state_miner_available_balance(miner_id):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {'jsonrpc': "2.0",
               'method': "Filecoin.StateMinerAvailableBalance",
               'params': [miner_id, None],
               'id': 3}
    # sending post request and saving the response as response object
    r = requests.get(url=URL, data=json.dumps(payload), headers=headers)
    return r.json()


def initial_state_miner_info(miner_id):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {'jsonrpc': "2.0",
               'method': "Filecoin.StateMinerInfo",
               'params': [miner_id, None],
               'id': 3}
    # sending post request and saving the response as response object
    r = requests.get(url=URL, data=json.dumps(payload), headers=headers)
    return r.json()


def read_state(miner_id):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {'jsonrpc': "2.0",
               'method': "Filecoin.StateReadState",
               'params': [miner_id, None],
               'id': 3}
    # sending post request and saving the response as response object
    r = requests.get(url=URL, data=json.dumps(payload), headers=headers)
    return r.json()


def wallet_balance(miner_id):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {'jsonrpc': "2.0",
               'method': "Filecoin.WalletBalance",
               'params': [miner_id],
               'id': 3}
    # sending post request and saving the response as response object
    r = requests.get(url=URL, data=json.dumps(payload), headers=headers)
    return r.json()


def state_miner_active_sectors(miner_id):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {'jsonrpc': "2.0",
               'method': "Filecoin.StateMinerActiveSectors",
               'params': [miner_id, None],
               'id': 3}
    # sending post request and saving the response as response object
    r = requests.get(url=URL, data=json.dumps(payload), headers=headers)
    return r.json()


def state_miner_sector_count(miner_id):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {'jsonrpc': "2.0",
               'method': "Filecoin.StateMinerSectorCount",
               'params': [miner_id, None],
               'id': 3}
    # sending post request and saving the response as response object
    r = requests.get(url=URL, data=json.dumps(payload), headers=headers)
    return r.json()
