
from flask import Blueprint, request, Response, render_template

import api.interpretation as api

interp_bp = Blueprint('interpretation', __name__)


### by type, calendar year, and number

@interp_bp.route('/<doc_type>/<int:year>/<int:number>/metadata', defaults={'version': None}, endpoint='current')
@interp_bp.route('/<doc_type>/<int:year>/<int:number>/welsh/metadata', defaults={'version': None}, endpoint='current-cy')
@interp_bp.route('/<doc_type>/<int:year>/<int:number>/<ver:version>/metadata', endpoint='version')
@interp_bp.route('/<doc_type>/<int:year>/<int:number>/<ver:version>/welsh/metadata', endpoint='version-cy')
def interpretation_by_calendar_year(doc_type, year, number, version):
    welsh = request.path.endswith('/welsh/metadata')
    return _interpretation_by_anything(doc_type, year, number, version, welsh)


@interp_bp.route('/<doc_type>/<int:year>/<int:number>/metadata/data.<fmt:fmt>', defaults={'version': None}, endpoint='current-data')
@interp_bp.route('/<doc_type>/<int:year>/<int:number>/welsh/metadata/data.<fmt:fmt>', defaults={'version': None}, endpoint='current-data-cy')
@interp_bp.route('/<doc_type>/<int:year>/<int:number>/<ver:version>/metadata/data.<fmt:fmt>', endpoint='version-data')
@interp_bp.route('/<doc_type>/<int:year>/<int:number>/<ver:version>/welsh/metadata/data.<fmt:fmt>', endpoint='version-data-cy')
def interpretation_data_by_calendar_year(doc_type, year, number, version, fmt):
    welsh = '/welsh/metadata/' in request.path
    return _interpretation_data_by_anything(doc_type, year, number, version, fmt, welsh)


### by type, calendar year, date, and number

@interp_bp.route('/<doc_type>/<int:year>/<date>/<int:number>/metadata', defaults={'version': None})
@interp_bp.route('/<doc_type>/<int:year>/<date>/<int:number>/<ver:version>/metadata')
def interpretation_by_calendar_year_and_date(doc_type, year, date, number, version):
    middle = f'{year}/{date}'
    return _interpretation_by_anything(doc_type, middle, number, version)


@interp_bp.route('/<doc_type>/<int:year>/<date>/<int:number>/metadata/data.<fmt:fmt>', defaults={'version': None})
@interp_bp.route('/<doc_type>/<int:year>/<date>/<int:number>/<ver:version>/metadata/data.<fmt:fmt>')
def interpretation_data_by_calendar_year_and_date(doc_type, year, date, number, version, fmt):
    middle = str(year) + '/' + date
    return _interpretation_data_by_anything(doc_type, middle, number, version, fmt)


### by type, regnal year, and number

@interp_bp.route('/<doc_type>/<reign>/<session>/<number>/metadata', defaults={'version': None}, endpoint='regnal-current')
@interp_bp.route('/<doc_type>/<reign>/<session>/<number>/<ver:version>/metadata', endpoint='regnal-version')
def interpretation_by_regnal_year(doc_type, reign, session, number, version):
    middle = f'{reign}/{session}'
    return _interpretation_by_anything(doc_type, middle, number, version)


@interp_bp.route('/<doc_type>/<reign>/<session>/<number>/metadata/data.<fmt:fmt>', defaults={'version': None}, endpoint='regnal-current-data')
@interp_bp.route('/<doc_type>/<reign>/<session>/<number>/<ver:version>/metadata/data.<fmt:fmt>', endpoint='regnal-version-data')
def interpretation_data_by_regnal_year(doc_type, reign, session, number, version, fmt):
    regnal = f'{reign}/{session}'
    return _interpretation_data_by_anything(doc_type, regnal, number, version, fmt)


### by type, regnal year, statute, and number

@interp_bp.route('/<doc_type>/<reign>/<session>/<statute>/<number>/metadata', defaults={'version': None})
@interp_bp.route('/<doc_type>/<reign>/<session>/<statute>/<number>/<ver:version>/metadata')
def interpretation_by_regnal_year_and_statute(doc_type, reign, session, statute, number, version):
    middle = f'{reign}/{session}/{statute}'
    return _interpretation_by_anything(doc_type, middle, number, version)


@interp_bp.route('/<doc_type>/<reign>/<session>/<statute>/<number>/metadata/data.<fmt:fmt>', defaults={'version': None})
@interp_bp.route('/<doc_type>/<reign>/<session>/<statute>/<number>/<ver:version>/metadata/data.<fmt:fmt>')
def interpretation_data_by_regnal_year_and_statute(doc_type, reign, session, statute, number, version, fmt):
    middle = f'{reign}/{session}/{statute}'
    return _interpretation_data_by_anything(doc_type, middle, number, version, fmt)


# aep/tempincert with and without number

@interp_bp.route('/aep/tempincert/<statute>/<int:number>/metadata')
@interp_bp.route('/aep/tempincert/<statute>/metadata', defaults={'number': None})
def aep_tempincert(statute, number):
    return _interpretation_by_anything('aep', statute, number, None)

@interp_bp.route('/aep/tempincert/<statute>/<int:number>/metadata/data.<fmt:fmt>')
@interp_bp.route('/aep/tempincert/<statute>/metadata/data.<fmt:fmt>', defaults={'number': None})
def aep_tempincert_data(statute, number, fmt):
    return _interpretation_data_by_anything('aep', statute, number, None, fmt)


### EU treaties

@interp_bp.route('/eut/<name>/metadata', defaults={'version': None})
@interp_bp.route('/eut/<name>/adopted/metadata', defaults={'version': 'adopted'})
def eu_treaty(name, version):
    return _interpretation_by_anything('eut', name, None, version)

@interp_bp.route('/eut/<name>/metadata/data.<fmt:fmt>', defaults={'version': None})
@interp_bp.route('/eut/<name>/adopted/metadata/data.<fmt:fmt>', defaults={'version': 'adopted'})
def eu_treaty_data(name, version, fmt):
    return _interpretation_data_by_anything('eut', name, None, version, fmt)


### helpers

def _interpretation_by_anything(doc_type, middle, number, version, welsh = False):
    interp = api.fetch_interpretation(doc_type, middle, number, version, welsh)
    title = interp.get('shortTitle')
    if title is None:
        title = interp.get('longTitle')
    return render_template('pages/interpretation.html', interp=interp, title=title)


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

def _interpretation_data_by_anything(doc_type, middle, number, version, fmt, welsh = False):
    mime = get_mimetype(fmt)
    data = api.fetch_interpretation_format(doc_type, middle, number, version, mime, welsh)
    return Response(data, mimetype=mime)


###

# these are redundant but could be added for API documentation
# @interp_bp.route('/aep/<reign>/<statute>/<number>/metadata', defaults={'version': None})
# @interp_bp.route('/aep/<reign>/<statute>/<number>/<version>/metadata')
# def interpretation_by_regnal_year_and_statute(reign, statute, number, version):
#     middle = reign + '/' + statute
#     return _interpretation_by_either('aep', middle, number, statute, version)
