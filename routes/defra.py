
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
    enhance_status_counts(data)
    enhance_year_counts(data)
    enhance_type_counts(data)
    enhance_chapter_counts(data)
    enhance_extent_counts(data)
    enhance_source_counts(data)
    enhance_regulator_counts(data)
    enhance_subject_counts(data)
    enhance_review_counts(data)
    data['grouped'] = {
        'byYear': group_year_counts(data),
        'byReviewDate': group_review_counts(data)
    }
    data['cancel_links'] = make_cancel_links(data)
    pager = pagination_data(
        current = data['query']['page'],
        total = pages_needed(data['counts']['total'], data['query']['pageSize']),
        base_endpoint = request.base_url,
        extra_params = prune_params(data['query'], 'page'),
        window = 4
    )
    return render_template('defra/main.html', data=data, pager=pager)


# add links to counts

def enhance_status_counts(data):
    add_links_to_counts(data, 'status', 'byStatus')


def enhance_year_counts(data):
    add_links_to_year_counts(data, 'year', 'byYear')


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
    add_links_to_year_counts(data, 'review', 'byReviewDate')


def add_links_to_counts(data, queryParam, countsKey):
    base = request.base_url + '?'
    other_params = prune_params(data['query'], queryParam)
    if other_params:
        base += urlencode(other_params) + '&'
    for count in  data['counts'][countsKey]:
        count['link'] = base + queryParam + '=' + count['id']


def add_links_to_year_counts(data, queryParam, countsKey):
    base = request.base_url + '?'
    other_params = prune_params(data['query'], queryParam)
    if other_params:
        base += urlencode(other_params) + '&'
    for count in  data['counts'][countsKey]:
        count['link'] = base + queryParam + '=' + str(count['year'])


# group yearly counts

def group_year_counts(data):
    return [list(batch) for batch in batched(data['counts']['byYear'], 12)]

def group_review_counts(data):
    return [list(batch) for batch in batched(data['counts']['byReviewDate'], 12)]


# make cancel links

def make_cancel_links(data):
    return {
        'status': make_cancel_link(data['query'], 'status'),
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
    if not params:
        return base
    return base + '?' + urlencode(params)


def prune_params(query, key):
    params = { k: v for k, v in query.items() if k != key and v is not None }
    params = { k: v for k, v in params.items() if k != 'page' and k != 'pageSize' }
    return params
