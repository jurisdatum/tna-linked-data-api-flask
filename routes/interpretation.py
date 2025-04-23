
from flask import Blueprint, Response, render_template

from api.interpretation import fetch_interpretation, fetch_interpretation_format

interp_bp = Blueprint('interpretation', __name__)

@interp_bp.route('/<doc_type>/<int:year>/<int:number>/metadata', defaults={'version': None})
@interp_bp.route('/<doc_type>/<int:year>/<int:number>/<version>/metadata')
def interpretation_by_calendar_year(doc_type, year, number, version):
    return _interpretation_by_either(doc_type, year, number, version)


@interp_bp.route('/<doc_type>/<reign>/<session>/<int:number>/metadata', defaults={'version': None})
@interp_bp.route('/<doc_type>/<reign>/<session>/<int:number>/<version>/metadata')
def interpretation_by_regnal_year(doc_type, reign, session, number, version):
    regnal = reign + '/' + session
    return _interpretation_by_either(doc_type, regnal, number, version)


def _interpretation_by_either(doc_type, year, number, version):
    interp = fetch_interpretation(doc_type, year, number, version)
    title = interp.get('shortTitle', interp.get('orderTitle'))
    return render_template('pages/interpretation.html', interp=interp, title=title)

# data

@interp_bp.route('/<doc_type>/<int:year>/<int:number>/metadata/data.<fmt:fmt>', defaults={'version': None})
@interp_bp.route('/<doc_type>/<int:year>/<int:number>/<version>/metadata/data.<fmt:fmt>')
def interpretation_data_by_calendar_year(doc_type, year, number, version, fmt):
    return _interpretation_data_by_either(doc_type, year, number, version, fmt)


@interp_bp.route('/<doc_type>/<reign>/<session>/<int:number>/metadata/data.<fmt:fmt>', defaults={'version': None})
@interp_bp.route('/<doc_type>/<reign>/<session>/<int:number>/<version>/metadata/data.<fmt:fmt>')
def interpretation_data_by_regnal_year(doc_type, reign, session, number, version, fmt):
    regnal = reign + '/' + session
    return _interpretation_data_by_either(doc_type, regnal, number, version, fmt)


_MIME_TYPES = {
    'rdf':     'application/rdf+xml',
    'rdfjson': 'application/rdf+json',
    'ttl':     'text/turtle',
    'json':    'application/json',
    'xml':     'application/xml',
    'jsonld':  'application/ld+json'
}
def get_mimetype(fmt):
    return _MIME_TYPES.get(fmt)

def _interpretation_data_by_either(doc_type, year, number, version, fmt):
    mime = get_mimetype(fmt)
    data = fetch_interpretation_format(doc_type, year, number, version, mime)
    return Response(data, mimetype=mime)
