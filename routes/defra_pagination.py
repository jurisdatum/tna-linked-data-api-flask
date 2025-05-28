
from urllib.parse import urlencode

def build_url(base_endpoint, page, extra_params=None):
    params = {} if extra_params is None else dict(extra_params)
    params["page"] = page
    return f"{base_endpoint}?{urlencode(params)}"


def pages_needed(total_items, per_page):
    """Return the number of pages required to display total_items items."""
    return (total_items + per_page - 1) // per_page   # or # -(-total_items // per_page),


def pagination_data(*, current, total, base_endpoint, extra_params=None, window=4):

    first = max(1, current - window)
    last  = min(total, current + window)

    pages = [
        {
            "num": p,
            "url": build_url(base_endpoint, p, extra_params),
            "is_current": p == current,
        }
        for p in range(first, last + 1)
    ]

    return {
        "has_prev": current > 1,
        "has_next": current < total,
        "prev_url": build_url(base_endpoint, current - 1, extra_params) if current > 1 else None,
        "next_url": build_url(base_endpoint, current + 1, extra_params) if current < total else None,
        "pages": pages
    }
