from flask import Flask, Response, render_template

from api import fetch_interpretation, fetch_interpretation_format
from routes.items import items_bp

app = Flask(__name__)

app.register_blueprint(items_bp)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/<type>/<int:year>/<int:number>/metadata')
def interpretation(type, year, number):
    meta = fetch_interpretation(type, year, number)
    return render_template('interpretation.html', interp=meta)

@app.route('/<type>/<int:year>/<int:number>/metadata/data.rdf')
def interpretation_rdf_xml(type, year, number):
    return data(type, year, number, 'application/rdf+xml')

@app.route('/<type>/<int:year>/<int:number>/metadata/data.json')
def interpretation_json(type, year, number):
    return data(type, year, number, 'application/json')

@app.route('/<type>/<int:year>/<int:number>/metadata/data.xml')
def interpretation_xml(type, year, number):
    return data(type, year, number, 'application/xml')

@app.route('/<type>/<int:year>/<int:number>/metadata/data.ttl')
def interpretation_turtle(type, year, number):
    return data(type, year, number, 'text/turtle')

def data(type, year, number, format):
    data = fetch_interpretation_format(type, year, number, format)
    resp = Response(data)
    resp.mimetype = format
    return resp
