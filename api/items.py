
from typing import Optional

from api.api import get, get_json

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