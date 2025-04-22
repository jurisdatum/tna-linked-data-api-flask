
from typing import Optional

import requests

_base_url = 'http://localhost:8080'


def get(endpoint: str, accept: str) -> requests.Response:
    url = _base_url + endpoint
    headers = { 'Accept': accept }
    return requests.get(url, headers=headers)

def get_json(endpoint: str) -> dict:
    return get(endpoint, 'application/json').json()


# items

def make_items_url(type, year, page: Optional[str]) -> str:
    url = '/ld/items/' + type + '/' + str(year)
    if (page):
        url += '?page=' + page
    return url

def fetch_items(type, year, page: Optional[str]) -> dict:
    url = make_items_url(type, year, page)
    return get_json(url)

def fetch_items_format(type, year, page: Optional[str], accept) -> str:
    url = make_items_url(type, year, page)
    return get(url, accept).text


# interpretation

def make_interpretation_url(type, year, number, version: Optional[str]) -> str:
    url = '/ld/interpretation/' + type + '/' + str(year) + '/' + str(number)
    if version:
        url += '?version=' + version
    return url

def fetch_interpretation(type, year, number, version: Optional[str]) -> dict:
    url = make_interpretation_url(type, year, number, version)
    return get_json(url)

def fetch_interpretation_format(type, year, number, version: Optional[str], accept) -> str:
    url = make_interpretation_url(type, year, number, version)
    return get(url, accept).text
