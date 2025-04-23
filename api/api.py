
import requests

_base_url = 'http://localhost:8080'


def get(endpoint: str, accept: str) -> requests.Response:
    url = _base_url + endpoint
    headers = { 'Accept': accept }
    return requests.get(url, headers=headers)


def get_json(endpoint: str) -> dict:
    return get(endpoint, 'application/json').json()
