
from flask import Blueprint, Response, render_template, request

from api import fetch_items, fetch_items_format
from routes.interpretation import get_mimetype

items_bp = Blueprint('items', __name__)

@items_bp.route('/<type>/<int:year>/metadata')
def items(type, year):
    page = request.args.get('page')
    data = fetch_items(type, year, page)
    title = make_page_title(type, year)
    query_string = '?page=' + page if page else None
    return render_template('pages/items.html', page=data, title=title, query_string=query_string)


@items_bp.route('/<type>/<int:year>/metadata/data.<fmt:fmt>')
def items_data(type, year, fmt):
    page = request.args.get('page')
    mime = get_mimetype(fmt)
    data = fetch_items_format(type, year, page, mime)
    return Response(data, mimetype=mime)

#

plural_type_labels = {
    'ukpga': 'UK Public General Acts',
    'ukla': 'UK Local Acts',
    'ukppa': 'UK Private and Personal Acts',
    'asp': 'Acts of the Scottish Parliament',
    'nia': 'Acts of the Northern Ireland Assembly',
    'aosp': 'Acts of the Old Scottish Parliament',
    'aep': 'Acts of the English Parliament',
    'aip': 'Acts of the Old Irish Parliament',
    'apgb': 'Acts of the Parliament of Great Britain',
    'gbla': 'Local Acts of the Parliament of Great Britain',
    'gbppa': '???',  # ToDo
    'anaw': 'Acts of the National Assembly for Wales',
    'asc': 'Acts of Senedd Cymru',
    'mwa': 'Measures of the National Assembly for Wales',
    'ukcm': 'Church Measures',
    'mnia': 'Measures of the Northern Ireland Assembly',
    'apni': 'Acts of the Northern Ireland Parliament',
    'uksi': 'UK Statutory Instruments',
    'ukmd': 'UK Ministerial Directions',
    'ukmo': 'UK Ministerial Orders',
    'uksro': 'UK Statutory Rules and Orders',
    'wsi': 'Wales Statutory Instruments',
    'ssi': 'Scottish Statutory Instruments',
    'nisi': 'Northern Ireland Orders in Council',
    'nisr': 'Northern Ireland Statutory Rules',
    'ukci': 'Church Instruments',
    'nisro': 'Northern Ireland Statutory Rules and Orders',

    'ukdsi': 'UK Draft Statutory Instruments',
    'sdsi': 'Scottish Draft Statutory Instruments',
    'nidsr': 'Northern Ireland Draft Statutory Rules',

    'eur': 'Regulations originating from the EU',
    'eudn': 'Decisions originating from the EU',
    'eudr': 'Directives originating from the EU'
}

def make_page_title(type, year):
    return plural_type_labels[type] + ' from ' + str(year)
