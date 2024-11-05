import requests

base_url = "https://pokeapi.co/api/v2/"

def get_info(name):
  url = f"{base_url}/pokemon/{name}"
  response = requests.get(url) 

  if response.status_code == 200: # if response was ok
    pokemon_data = response.json()  # converts response into json and python dict
    return pokemon_data

  else:
    print(f"failed to retrieve data {response.status_code}")

pokemon_name = "charizard"
info = get_info(pokemon_name) # gets back dictionary on success

if info:
  print(info["name"])
  print(info["id"])
  print(info["height"])
  print(info["weight"])

