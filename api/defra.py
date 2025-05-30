
from datetime import date
from urllib.parse import urlencode

from api.api import get_json


def fetch(*, inForce=None, type=None, year=None, chapter=None, extent=None, source=None,
          regulator=None, subject=None, review=None, page=None, pageSize=None) -> dict:
    params = {k: v for k, v in locals().items() if v is not None}
    url = '/defra/items?' + urlencode(params)
    results = get_json(url)
    for item in results['results']:
        value = item['review']
        if value is not None:
            item['review'] = date.fromisoformat(value)
    return results
