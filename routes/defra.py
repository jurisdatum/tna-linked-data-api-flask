
import inspect
from itertools import batched
from urllib.parse import urlencode

from flask import Blueprint, redirect, render_template, request

from api.defra import fetch
from routes.defra_pagination import pages_needed, pagination_data


defra_bp = Blueprint('defra', __name__)


@defra_bp.route('/defralex')
def defra():
    return redirect('/defralex/lists')


@defra_bp.route('/defralex/lists')
def defra_lists():
    sig = inspect.signature(fetch)
    allowed_keys = set(sig.parameters.keys())
    filtered_args = { key: request.args[key] for key in request.args if key in allowed_keys }
    data = fetch(**filtered_args)
    enhance_counts(data)
    data['grouped'] = group_counts(data)
    data['cancel_links'] = make_cancel_links(data)
    data['exclude_comm_orders_link'] = make_exclude_comm_orders_link(data)
    data['exclude_rev_orders_link'] = make_exclude_rev_orders_link(data)
    pager = pagination_data(
        current = data['query']['page'],
        total = pages_needed(data['counts']['total'], data['query']['pageSize']),
        base_endpoint = request.base_url,
        extra_params = prune_params(data['query'], 'page'),
        window = 4
    )
    return render_template('defra/main.html', data=data, pager=pager)


# add links to counts

def enhance_counts(data):
    enhance_in_force_counts(data)
    enhance_year_counts(data)
    enhance_type_counts(data)
    enhance_chapter_counts(data)
    enhance_extent_counts(data)
    enhance_source_counts(data)
    enhance_regulator_counts(data)
    enhance_subject_counts(data)
    enhance_review_counts(data)


def enhance_in_force_counts(data):
    add_links_to_counts(data, 'inForce', 'byInForce', 'value')
    for count in  data['counts']['byInForce']:
        if count['value']:
            count['label'] = 'In Force'
        else:
            count['label'] = 'Not In Force'


def enhance_year_counts(data):
    add_links_to_counts(data, 'year', 'byYear', 'year')


def enhance_type_counts(data):
    add_links_to_counts(data, 'type', 'byType')


def enhance_chapter_counts(data):
    add_links_to_counts(data, 'chapter', 'byChapter')


def enhance_extent_counts(data):
    add_links_to_counts(data, 'extent', 'byExtent')


def enhance_source_counts(data):
    add_links_to_counts(data, 'source', 'bySource')


def enhance_regulator_counts(data):
    add_links_to_counts(data, 'regulator', 'byRegulator')


def enhance_subject_counts(data):
    add_links_to_counts(data, 'subject', 'bySubject')


def enhance_review_counts(data):
    add_links_to_counts(data, 'review', 'byReviewDate', 'year')


def add_links_to_counts(data, queryParam, countsKey, countKey = 'id'):
    base = request.base_url + '?'
    other_params = prune_params(data['query'], queryParam)
    if other_params:
        base += urlencode(other_params) + '&'
    for count in  data['counts'][countsKey]:
        value = count[countKey]
        if isinstance(value, bool):
            value = str(value).lower()
        elif isinstance(value, int):
            value = str(value)
        count['link'] = base + queryParam + '=' + value


def make_exclude_comm_orders_link(data):
    params = prune_params(data['query'], 'inForce')
    params['inForce'] = 'true'
    params['isCommencementOrder'] = 'false'
    return request.base_url + '?' + urlencode(params)

def make_exclude_rev_orders_link(data):
    params = prune_params(data['query'], 'inForce')
    params['inForce'] = 'true'
    params['isRevocationOrder'] = 'false'
    return request.base_url + '?' + urlencode(params)


# group yearly counts

def group_counts(data):
    return {
        'byYear': group_year_counts(data),
        'byReviewDate': group_review_counts(data)
    }

def group_year_counts(data):
    return [list(batch) for batch in batched(data['counts']['byYear'], 12)]

def group_review_counts(data):
    return [list(batch) for batch in batched(data['counts']['byReviewDate'], 12)]


# make cancel links

def make_cancel_links(data):
    return {
        'inForce': make_cancel_link(data['query'], 'inForce'),
        'isCommencementOrder': make_cancel_link(data['query'], 'isCommencementOrder'),
        'isRevocationOrder': make_cancel_link(data['query'], 'isRevocationOrder'),
        'year': make_cancel_link(data['query'], 'year'),
        'type': make_cancel_link(data['query'], 'type'),
        'chapter': make_cancel_link(data['query'], 'chapter'),
        'extent': make_cancel_link(data['query'], 'extent'),
        'source': make_cancel_link(data['query'], 'source'),
        'regulator': make_cancel_link(data['query'], 'regulator'),
        'subject': make_cancel_link(data['query'], 'subject'),
        'review': make_cancel_link(data['query'], 'review')
    }

def make_cancel_link(query, key):
    base = request.base_url
    params = prune_params(query, key)
    if key == 'inForce':
        params.pop('isCommencementOrder', None)
        params.pop('isRevocationOrder', None)
    if not params:
        return base
    return base + '?' + urlencode(params)


def prune_params(query, key):
    return {
        k: str(v).lower() if isinstance(v, bool) else v
        for k, v in query.items()
        if k != key and v is not None and k != 'page' and k != 'pageSize'
    }
