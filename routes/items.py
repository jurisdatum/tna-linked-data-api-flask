
from flask import Blueprint, Response, render_template, request

from flask_babel import lazy_gettext as _

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
    'ukpga': _('UK Public General Acts'),
    'ukla': _('UK Local Acts'),
    'ukppa': _('UK Private and Personal Acts'),
    'asp': _('Acts of the Scottish Parliament'),
    'nia': _('Acts of the Northern Ireland Assembly'),
    'aosp': _('Acts of the Old Scottish Parliament'),
    'aep': _('Acts of the English Parliament'),
    'aip': _('Acts of the Old Irish Parliament'),
    'apgb': _('Acts of the Parliament of Great Britain'),
    'gbla': _('Local Acts of the Parliament of Great Britain'),
    'gbppa': _('???'),  # ToDo
    'anaw': _('Acts of the National Assembly for Wales'),
    'asc': _('Acts of Senedd Cymru'),
    'mwa': _('Measures of the National Assembly for Wales'),
    'ukcm': _('Church Measures'),
    'mnia': _('Measures of the Northern Ireland Assembly'),
    'apni': _('Acts of the Northern Ireland Parliament'),
    'uksi': _('UK Statutory Instruments'),
    'ukmd': _('UK Ministerial Directions'),
    'ukmo': _('UK Ministerial Orders'),
    'uksro': _('UK Statutory Rules and Orders'),
    'wsi': _('Wales Statutory Instruments'),
    'ssi': _('Scottish Statutory Instruments'),
    'nisi': _('Northern Ireland Orders in Council'),
    'nisr': _('Northern Ireland Statutory Rules'),
    'ukci': _('Church Instruments'),
    'nisro': _('Northern Ireland Statutory Rules and Orders'),

    'ukdsi': _('UK Draft Statutory Instruments'),
    'sdsi': _('Scottish Draft Statutory Instruments'),
    'nidsr': _('Northern Ireland Draft Statutory Rules'),

    'eur': _('Regulations originating from the EU'),
    'eudn': _('Decisions originating from the EU'),
    'eudr': _('Directives originating from the EU'),
}

def make_page_title(type, year):
    return plural_type_labels[type] + ' ' + _('from') + ' ' + str(year)
