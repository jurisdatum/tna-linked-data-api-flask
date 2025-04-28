
from api.api import get, get_json

def make_class_url(name: str) -> str:
    return '/ld/class/' + name


def fetch_class(name: str) -> dict:
    url = make_class_url(name)
    return get_json(url)


def fetch_class_format(name: str, accept: str) -> str:
    url = make_class_url(name)
    return get(url, accept).text
