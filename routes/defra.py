
import inspect
from itertools import batched
from urllib.parse import urlencode

from flask import Blueprint, render_template, request

from api.defra import fetch


defra_bp = Blueprint('defra', __name__)


@defra_bp.route('/defralex')
def defra():
    data = fetch()
    enhange_status_counts(data)
    data['grouped'] = {
        'byYear': enhance_year_counts(data)
    }
    data['cancel_links'] = make_cancel_links(data)
    return render_template('defra/main.html', data=data)


@defra_bp.route('/defralex/lists')
def defra_lists():
    sig = inspect.signature(fetch)
    allowed_keys = set(sig.parameters.keys())
    filtered_args = { key: request.args[key] for key in request.args if key in allowed_keys }
    data = fetch(**filtered_args)
    enhange_status_counts(data)
    data['grouped'] = {
        'byYear': enhance_year_counts(data)
    }
    data['cancel_links'] = make_cancel_links(data)
    return render_template('defra/main.html', data=data)



def enhange_status_counts(data):
    base = 'http://localhost:5000/defralex/lists?'
    other_params = prune_params(data['query'], 'status')
    if other_params:
        base += urlencode(other_params) + '&'
    for count in  data['counts']['byStatus']:
        count['link'] = base + 'status=' + str(count['id'])


def enhance_year_counts(data):
    base = 'http://localhost:5000/defralex/lists?'
    other_params = prune_params(data['query'], 'year')
    if other_params:
        base += urlencode(other_params) + '&'
    for count in  data['counts']['byYear']:
        count['link'] = base + 'year=' + str(count['year'])
    return [list(batch) for batch in batched(data['counts']['byYear'], 12)]


def make_cancel_links(data):
    return {
        'status': make_cancel_link(data['query'], 'status'),
        'year': make_cancel_link(data['query'], 'year')
    }

def make_cancel_link(query, key):
    base = 'http://localhost:5000/defralex/lists'
    params = prune_params(query, key)
    if not params:
        return base
    return base + '?' + urlencode(params)


def prune_params(query, key):
    params = { k: v for k, v in query.items() if k != key and v is not None }
    params = { k: v for k, v in params.items() if k != 'page' or v != 1 }
    params = { k: v for k, v in params.items() if k != 'pageSize' }
    return params
