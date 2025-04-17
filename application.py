
from flask import Flask

from routes.items import items_bp
from routes.interpretation import interp_bp

app = Flask(__name__)

app.register_blueprint(items_bp)
app.register_blueprint(interp_bp)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
