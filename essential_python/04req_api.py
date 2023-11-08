import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
resp = requests.get(url)
data = resp.json()

with open('pikachu.json', 'w') as f:
  json.dump(data, f)
