
import requests

from flask import current_app


def get(endpoint: str, accept: str, welsh: bool = False) -> requests.Response:
    base_url = current_app.config['API_BASE_URL']
    url = base_url + endpoint
    headers = { 'Accept': accept }
    if welsh:
        headers['Accept-Language'] = 'cy'
    return requests.get(url, headers=headers)


def get_json(endpoint: str, welsh: bool = False) -> dict:
    return get(endpoint, 'application/json', welsh).json()
