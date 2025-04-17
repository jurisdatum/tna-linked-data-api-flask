from flask import Blueprint, Response, render_template, request

from api import fetch_items, fetch_items_format

items_bp = Blueprint('items', __name__)

@items_bp.route('/<type>/<int:year>/metadata')
def items(type, year):
    page = request.args.get('page')
    data = fetch_items(type, year, page)
    title = make_page_title(type, year)
    query_string = '?page=' + page if page else None
    return render_template('items.html', page=data, title=title, query_string=query_string)


@items_bp.route('/<type>/<int:year>/metadata/data.rdf')
def items_rdf_xml(type, year):
    return items_data(type, year, 'application/rdf+xml')

@items_bp.route('/<type>/<int:year>/metadata/data.rdfjson')
def items_rdf_json(type, year):
    return items_data(type, year, 'application/rdf+json')

@items_bp.route('/<type>/<int:year>/metadata/data.ttl')
def items_turtle(type, year):
    return items_data(type, year, 'text/turtle')

@items_bp.route('/<type>/<int:year>/metadata/data.json')
def items_json(type, year):
    return items_data(type, year, 'application/json')

@items_bp.route('/<type>/<int:year>/metadata/data.xml')
def items_xml(type, year):
    return items_data(type, year, 'application/xml')

def items_data(type, year, format):
    page = request.args.get('page')
    data = fetch_items_format(type, year, page, format)
    resp = Response(data)
    resp.mimetype = format
    return resp

#

plural_type_labels = {
    'ukpga': 'UK Public General Acts'
}

def make_page_title(type, year):
    return plural_type_labels[type] + ' from ' + str(year)
