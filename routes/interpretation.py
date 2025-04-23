
from flask import Blueprint, Response, render_template

from api.interpretation import fetch_interpretation, fetch_interpretation_format

interp_bp = Blueprint('interpretation', __name__)

@interp_bp.route('/<doc_type>/<int:year>/<int:number>/metadata', defaults={'version': None})
@interp_bp.route('/<doc_type>/<int:year>/<int:number>/<version>/metadata')
def interpretation(doc_type, year, number, version):
    interp = fetch_interpretation(doc_type, year, number, version)
    title = title = interp.get('shortTitle', interp.get('orderTitle'))
    return render_template('pages/interpretation.html', interp=interp, title=title)


def get_mimetype(fmt):
    return {
        'rdf': 'application/rdf+xml',
        'rdfjson': 'application/rdf+json',
        'ttl': 'text/turtle',
        'json': 'application/json',
        'xml': 'application/xml',
    }.get(fmt)


@interp_bp.route('/<doc_type>/<int:year>/<int:number>/metadata/data.<fmt:fmt>', defaults={'version': None})
@interp_bp.route('/<doc_type>/<int:year>/<int:number>/<version>/metadata/data.<fmt:fmt>')
def interpretation_data(doc_type, year, number, version, fmt):
    mime = get_mimetype(fmt)
    data = fetch_interpretation_format(doc_type, year, number, version, mime)
    return Response(data, mimetype=mime)
