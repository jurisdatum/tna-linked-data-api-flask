
from typing import Optional

from api.api import get, get_json

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
