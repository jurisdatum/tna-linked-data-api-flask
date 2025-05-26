
import inspect

from flask import Blueprint, render_template, request

from api.defra import fetch
from routes.interpretation import get_mimetype

defra_bp = Blueprint('defra', __name__)


@defra_bp.route('/defralex')
def defra():
    data = fetch()
    return render_template('defra/main.html', data=data)


@defra_bp.route('/defralex/lists')
def defra_lists():
    sig = inspect.signature(fetch)
    allowed_keys = set(sig.parameters.keys())
    filtered_args = {
        key: request.args[key]
        for key in request.args
        if key in allowed_keys
    }
    data = fetch(**filtered_args)
    return render_template('defra/main.html', data=data)
