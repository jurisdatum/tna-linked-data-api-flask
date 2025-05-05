
from flask import Flask, render_template, request, url_for as flask_url_for
from flask_babel import Babel

from werkzeug.routing import BaseConverter

from routes.items import items_bp
from routes.interpretation import interp_bp
from routes.clazz import class_bp


class FormatConverter(BaseConverter):
    regex = 'json|xml|ttl|rdf|rdfjson|jsonld'


app = Flask(__name__)

app.config.from_object('config')
app.config.from_prefixed_env(prefix='LGU2')  # allow override via env

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'cy']

app.url_map.converters['fmt'] = FormatConverter


def get_locale():
    parts = request.path.strip('/').split('/')
    if parts and parts[0] == 'cy':
        return 'cy'
    return 'en'

babel = Babel(app, locale_selector=get_locale)

@app.context_processor
def inject_get_locale():
    return dict(get_locale=get_locale)

app.add_url_rule('/id/<path:rest>', redirect_to='/<rest>', endpoint='strip_id')
app.add_url_rule('/cy/id/<path:rest>', redirect_to='/cy/<rest>', endpoint='strip_id_cy')

app.register_blueprint(items_bp)
app.register_blueprint(interp_bp)
app.register_blueprint(class_bp)
app.register_blueprint(items_bp, name_prefix='welsh_', url_prefix='/cy')
app.register_blueprint(interp_bp, name_prefix='welsh_', url_prefix='/cy')
app.register_blueprint(class_bp, name_prefix='welsh_', url_prefix='/cy')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('404.html'), 500


@app.context_processor
def inject_localized_url_generator():
    """
    Injects a url_for function that adds locale prefixes if needed.
    Overrides the default url_for in templates.
    """
    def localized_url_for(endpoint, **values):
        """
        Generates a URL for the given endpoint.
        If the current locale is not the default locale, it prepends
        the locale code (e.g., '/cy') to the URL path.
        """
        # Pop _external before generating the base URL path
        is_external = values.pop('_external', False)

        # Generate the base URL using Flask's original url_for
        url = flask_url_for(endpoint, _external=False, **values) # Generate path only first

        current_locale = get_locale()
        default_locale = app.config.get('BABEL_DEFAULT_LOCALE', 'en')

        # Add prefix if the locale is active and not the default
        if current_locale and str(current_locale) != default_locale:
            url = f'/{current_locale}{url}'

        # If _external was requested, generate the full URL *now*
        # We do this *after* potentially adding the prefix to the path part.

        ### During development, I'll treat all URLs as external! (Jim)

        if is_external or True:
            # Regenerate the URL with the (potentially prefixed) path and _external=True
            # Note: This re-calls url_for with the *same endpoint and values*,
            # but relies on the fact that Flask constructs the external URL correctly
            # using SERVER_NAME etc. The *path* part has already been determined above.
            # A simpler way might be to just join the scheme/domain if needed manually,
            # but letting url_for handle _external=True is generally more robust.
            # However, generating the base path first and then prepending is key.

            # Let's reconstruct the external URL carefully
            # Get the scheme and netloc from a dummy external URL
            dummy_external_url = flask_url_for(endpoint, _external=True, **values)
            from urllib.parse import urlparse, urlunparse
            parsed_dummy = urlparse(dummy_external_url)

            # Use the scheme and netloc from the dummy, but our potentially prefixed path
            # This assumes the non-external url starts with '/'
            url = urlunparse((parsed_dummy.scheme, parsed_dummy.netloc, url, '', '', ''))


        return url

    # Return the function, making it available as 'url_for' in Jinja
    # You could use a different name like 'lurl_for' to avoid overriding
    # the default if you prefer, but overriding is common for this use case.
    return dict(url_for=localized_url_for)
