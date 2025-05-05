
import requests

_base_url = 'http://localhost:8080'


def get(endpoint: str, accept: str, welsh: bool = False) -> requests.Response:
    url = _base_url + endpoint
    headers = { 'Accept': accept }
    if welsh:
        headers['Accept-Language'] = 'cy'
    return requests.get(url, headers=headers)


def get_json(endpoint: str, welsh: bool = False) -> dict:
    return get(endpoint, 'application/json', welsh).json()
