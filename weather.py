# MUNICIPALITY in AIRPORT = CITY NAME
import requests

api_key = "543cd516ab7095dab8faac0cf1a3731d"

def sää(municipality):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"
    vastaus = requests.get(url)
    data = vastaus.json()

    if vastaus.status_code == 200:
        kelvin_temp = data["main"]["temp"]
        celsius_temp = kelvin_temp - 273.15 # muuttaa noudetun celciouksiksi
        description = data["weather"][0]["description"]
        return {"city": municipality, "temp": celsius_temp, "description": description}
