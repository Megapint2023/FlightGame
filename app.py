from flask import Flask, jsonify
from flask_cors import CORS
from yhteys import database_query

app = Flask(__name__)
CORS(app)

@app.route("/countries")
def get_countries():
    query = "SELECT name FROM country WHERE continent = 'EU' ORDER BY name;"
    results = database_query(query)
    country_list = [row[0] for row in results]
    return jsonify(country_list)

@app.route("/airports")
def get_airports():
    query = (
        "SELECT airport.name, airport.ident, airport.latitude_deg, airport.longitude_deg "
        "FROM airport "
        "JOIN country ON airport.iso_country = country.iso_country "
        "WHERE airport.type = 'large_airport' AND country.continent = 'EU' "
        "AND country.iso_country != 'RU';"
    )
    results = database_query(query)
    airport_list = [
        {
            "name": row[0],
            "icao": row[1],
            "lat": float(row[2]),
            "lon": float(row[3]),
        }
        for row in results
    ]
    return jsonify(airport_list)

if __name__ == "__main__":
    app.run(debug=True)