
import requests

hakusana = input("Anna hakusana: ")


pyyntö = "https://api.openweathermap.org/data/2.5/weather?q=" + hakusana+ "&units=metric&lang=FI&appid=26d0a02da6a5c39a839bf04976b49eac"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
    print(f"Sijainnin {hakusana} lämpötila: {json_vastaus['main']['temp']} °C")
    print(f"Sään kuvaus: {json_vastaus['weather'][0]['description']}")

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")



