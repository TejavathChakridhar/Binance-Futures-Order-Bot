import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from .config import API_KEY, API_SECRET, BASE_URL, RECV_WINDOW

HEADERS = {'X-MBX-APIKEY': API_KEY}

def _get_timestamp_ms():
    return int(time.time() * 1000)

def sign_payload(payload: dict) -> str:
    query_string = urlencode(payload)
    signature = hmac.new(API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    return signature

def send_signed_request(http_method: str, url_path: str, payload: dict = None):
    if payload is None:
        payload = {}
    payload.update({'timestamp': _get_timestamp_ms(), 'recvWindow': RECV_WINDOW})
    signature = sign_payload(payload)
    payload['signature'] = signature
    url = BASE_URL + url_path
    if http_method.upper() == 'GET':
        r = requests.get(url, headers=HEADERS, params=payload, timeout=10)
    else:
        r = requests.post(url, headers=HEADERS, params=payload, timeout=10)
    r.raise_for_status()
    return r.json()

def send_public_request(http_method: str, url_path: str, params: dict = None):
    url = BASE_URL + url_path
    if params is None:
        params = {}
    if http_method.upper() == 'GET':
        r = requests.get(url, params=params, timeout=10)
    else:
        r = requests.post(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()
