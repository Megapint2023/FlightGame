import requests
import json

hakusana = input("Anna paikkakunta: ")
api_key = "543cd516ab7095dab8faac0cf1a3731d"

pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid={api_key}"
vastaus = requests.get(pyyntö)
data = vastaus.json()

if vastaus.status_code == 200: # code 200 tarkoittaa onnistunut, 404/401 ei löydy tai virhe API
    #data = vastaus.json()
    #print(json.dumps(data, indent=2)) # tämä sylkee printin ns. hienommaksi

    kelvin_temp = data["main"]["temp"] # suodattaa vastauksesta tarvittavat, muuten liikaa tietoa
    celsius_temp = kelvin_temp - 273.15 # muuttaa tehtävän pyydetty celsius

    print(f"Sää kaupungissa: {hakusana}:")
    print(f"Lämpötila: {celsius_temp:.2f}°C")
    print(f"Kuvaus: {data['weather'][0]['description']}")
else:
    print("Virhe.")