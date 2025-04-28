
from flask import Blueprint, Response, render_template

from api.clazz import fetch_class, fetch_class_format
from routes.interpretation import get_mimetype

class_bp = Blueprint('clazz', __name__)

@class_bp.route('/def/legislation/<name>')
def clazz(name):
    data = fetch_class(name)
    return render_template('pages/clazz.html', clazz=data)

@class_bp.route('/def/legislation/<name>/data.<fmt:fmt>')
def clazz_data(name, fmt):
    mime = get_mimetype(fmt)
    data = fetch_class_format(name, mime)
    return Response(data, mimetype=mime)
