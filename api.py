from flask import Flask, jsonify
from flask_cors import CORS
from yhteys import database_query

app = Flask(__name__)
CORS(app)

@app.route("/countries")
def get_countries():
    query = "SELECT name FROM country WHERE continent = 'EU' ORDER BY name;"
    results = database_query(query)

    # results = [(Finland,), (Sweden,), ...]
    country_list = [row[0] for row in results]

    return jsonify(country_list)

if __name__ == "__main__":
    app.run(debug=True)