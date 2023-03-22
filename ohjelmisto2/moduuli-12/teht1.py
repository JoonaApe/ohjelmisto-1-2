import requests

pyynto = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyynto).json()
text = vastaus["value"]
print(text)