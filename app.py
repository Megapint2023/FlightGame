from flask import Flask, jsonify, request
from flask_cors import CORS
from yhteys import database_query
from game import Game_stats
from weather import sää
app = Flask(__name__)
CORS(app)
game = Game_stats("Player")

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    icao = data.get("icao")
    distance = data.get("distance")
    result = game.move(icao, distance)

    query = "SELECT municipality, iso_country FROM airport WHERE ident = %s"
    rows = database_query(query, (icao,))
    # CANCER FEST BEGINS HERE

    municipality = rows[0][0]
    country_code = rows[0][1]
    result["location"] = municipality
    result["country"] = country_code
    result["location"] = municipality
    if rows:
        weather = sää(municipality)
        result["weather"] = weather
    else:
        result["location"] = None
        result["country"] = None
        result["weather"] = None
    return jsonify(result)

@app.route("/airports")
def get_airports():
    query = (
        "SELECT airport.name, airport.ident, airport.latitude_deg, airport.longitude_deg, country.name "
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
            "country": row[4]
        }
        for row in results
    ]
    return jsonify(airport_list)

@app.route("/countries")
def get_countries():
    query = "SELECT name FROM country WHERE continent = 'EU' ORDER BY name;"
    results = database_query(query)
    country_list = [row[0] for row in results]
    return jsonify(country_list)
if __name__ == "__main__":
    app.run(debug=True)