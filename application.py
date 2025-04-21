
from flask import Flask, render_template, request
from flask_babel import Babel

from routes.items import items_bp
from routes.interpretation import interp_bp

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'cy']

def get_locale():
    parts = request.path.strip('/').split('/')
    if parts and parts[0] == 'cy':
        return 'cy'
    return 'en'

babel = Babel(app, locale_selector=get_locale)

@app.context_processor
def inject_get_locale():
    return dict(get_locale=get_locale)

app.register_blueprint(items_bp)
app.register_blueprint(interp_bp)
app.register_blueprint(items_bp, name_prefix='welsh_', url_prefix='/cy')
app.register_blueprint(interp_bp, name_prefix='welsh_', url_prefix='/cy')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('404.html'), 500
