from flask import Flask, jsonify, request
from flask_cors import CORS
from yhteys import database_query
from game import Game_stats
from weather import sää

app = Flask(__name__)
CORS(app)
game = Game_stats("Player")
game.suitcase()


@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    icao = data.get("icao")
    distance = data.get("distance")
    result = game.move(icao, distance)

    query = ("SELECT airport.municipality, country.name "
             "FROM airport "
             "JOIN country ON airport.iso_country = country.iso_country "
             "WHERE airport.ident = %s")

    results = database_query(query, (icao,))
    move_list = [
        {
            "location": row[0],
            "country": row[1],
            "weather": sää(row[0])
        }
        for row in results
    ]
    return jsonify({**result, **move_list[0]})


@app.route("/airports")
def get_airports():
    query = (
        "SELECT airport.name, airport.ident, airport.latitude_deg, "
        "airport.longitude_deg, country.name "
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

@app.route("/current_suitcase")
def current_suitcase():
    icao = game.suitcase_location
    query = (
        "SELECT latitude_deg, longitude_deg "
        "FROM airport "
        "WHERE ident = %s"
    )
    result = database_query(query, (icao,))
    lat, lon = result[0]
    suitcase_info = {
        "icao": icao,
        "lat": float(lat),
        "lon": float(lon)
    }
    return jsonify(suitcase_info)


if __name__ == "__main__":
    app.run(debug=True)