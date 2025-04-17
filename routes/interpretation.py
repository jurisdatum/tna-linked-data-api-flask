
from flask import Blueprint, Response, render_template, request

from api import fetch_interpretation, fetch_interpretation_format

interp_bp = Blueprint('interpretation', __name__)

@interp_bp.route('/<type>/<int:year>/<int:number>/metadata')
def interpretation(type, year, number):
    meta = fetch_interpretation(type, year, number)
    return render_template('pages/interpretation.html', interp=meta)

@interp_bp.route('/<type>/<int:year>/<int:number>/metadata/data.rdf')
def interpretation_rdf_xml(type, year, number):
    return data(type, year, number, 'application/rdf+xml')

@interp_bp.route('/<type>/<int:year>/<int:number>/metadata/data.rdfjson')
def interpretation_rdf_json(type, year, number):
    return data(type, year, number, 'application/rdf+json')

@interp_bp.route('/<type>/<int:year>/<int:number>/metadata/data.ttl')
def interpretation_turtle(type, year, number):
    return data(type, year, number, 'text/turtle')

@interp_bp.route('/<type>/<int:year>/<int:number>/metadata/data.json')
def interpretation_json(type, year, number):
    return data(type, year, number, 'application/json')

@interp_bp.route('/<type>/<int:year>/<int:number>/metadata/data.xml')
def interpretation_xml(type, year, number):
    return data(type, year, number, 'application/xml')

def data(type, year, number, format):
    data = fetch_interpretation_format(type, year, number, format)
    resp = Response(data)
    resp.mimetype = format
    return resp
