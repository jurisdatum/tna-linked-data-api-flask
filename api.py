
from typing import Any, Optional

import requests

_base_url = 'http://localhost:8080'


def get(endpoint: str, accept: str) -> requests.Response:
    url = _base_url + endpoint
    headers = { 'Accept': accept }
    return requests.get(url, headers=headers)

def get_json(endpoint: str) -> dict:
    return get(endpoint, 'application/json').json()


# items

def fetch_items(type, year, page: Optional[str]) -> dict:
    url = '/ld/items/' + type + '/' + str(year)
    if (page):
        url += '?page=' + page
    return get_json(url)

def fetch_items_format(type, year, page: Optional[str], accept) -> str:
    url = '/ld/items/' + type + '/' + str(year)
    if (page):
        url += '?page=' + page
    return get(url, accept).text


# interpretation

def fetch_interpretation(type, year, number) -> dict:
    url = '/ld/interpretation/' + type + '/' + str(year) + '/' + str(number)
    return get_json(url)

def fetch_interpretation_format(type, year, number, accept) -> str:
    url = '/ld/interpretation/' + type + '/' + str(year) + '/' + str(number)
    return get(url, accept).text
