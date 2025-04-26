from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

SOLR_URL = "http://localhost:8983/solr/mycollection/select"

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    params = {
        'q': f'name:{query}*',
        'wt': 'json',
        'rows': 10,
        'facet': 'true',
        'facet.field': 'category'
    }
    response = requests.get(SOLR_URL, params=params)
    results = response.json()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
