from flask import Flask, Response, render_template

from api import fetch_interpretation, fetch_interpretation_format

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test")
def test():
    return render_template('frame.html')


@app.route('/<type>/<int:year>/<int:number>/metadata')
def document_metadata(type, year, number):
    meta = fetch_interpretation(type, year, number)
    return render_template('interpretation.html', interp=meta)

@app.route('/<type>/<int:year>/<int:number>/metadata/data.rdf')
def document_metadata_rdf_xml(type, year, number):
    return document_metadata_format(type, year, number, 'application/rdf+xml')

@app.route('/<type>/<int:year>/<int:number>/metadata/data.json')
def document_metadata_json(type, year, number):
    return document_metadata_format(type, year, number, 'application/json')

@app.route('/<type>/<int:year>/<int:number>/metadata/data.xml')
def document_metadata_xml(type, year, number):
    return document_metadata_format(type, year, number, 'application/xml')

@app.route('/<type>/<int:year>/<int:number>/metadata/data.ttl')
def document_metadata_turtle(type, year, number):
    return document_metadata_format(type, year, number, 'text/turtle')

def document_metadata_format(type, year, number, format):
    data = fetch_interpretation_format(type, year, number, format)
    resp = Response(data)
    resp.mimetype = format
    return resp
