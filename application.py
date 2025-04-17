
from flask import Flask, render_template

from routes.items import items_bp
from routes.interpretation import interp_bp

app = Flask(__name__)

app.register_blueprint(items_bp)
app.register_blueprint(interp_bp)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('404.html'), 500
