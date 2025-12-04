from flask import Flask, Response
import json

app = Flask(__name__)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:x>')
def alkuluku(x):
    tulos = is_prime(x)
    tilakoodi = 200
    vastaus = {
        "Number": x,
        "isPrime": tulos
    }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": 404,
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)