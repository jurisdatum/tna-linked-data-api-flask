
from typing import Optional

from api.api import get, get_json

def _make_interpretation_url(type: str, middle: int|str, number: Optional[int|str], version: Optional[str]) -> str:
    url = '/ld/interpretation/' + type + '/' + str(middle)
    if number:
        url += '/' + str(number)
    if version:
        url += '?version=' + version
    return url


def fetch_interpretation(type: str, middle: int|str, number: Optional[int|str], version: Optional[str], welsh: bool = False) -> dict:
    url = _make_interpretation_url(type, middle, number, version)
    return get_json(url, welsh)


def fetch_interpretation_format(type: str, middle: int|str, number: Optional[int|str], version: Optional[str], accept, welsh: bool = False) -> str:
    url = _make_interpretation_url(type, middle, number, version)
    return get(url, accept, welsh).text
