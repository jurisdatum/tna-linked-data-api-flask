
from urllib.parse import urlencode

from api.api import get_json


def fetch(*, status=None, type=None, year=None, chapter=None, extent=None, source=None,
          regulator=None, subject=None, review=None, page=None, pageSize=None) -> dict:
    params = {k: v for k, v in locals().items() if v is not None}
    url = '/defra/items?' + urlencode(params)
    return get_json(url)
