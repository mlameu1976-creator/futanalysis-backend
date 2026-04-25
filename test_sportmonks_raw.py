import os
import requests

API_TOKEN = os.getenv("SPORTMONKS_API_TOKEN")

print("TOKEN:", API_TOKEN)

if not API_TOKEN:
    raise RuntimeError("TOKEN NÃO CARREGADO")

# DATA HISTÓRICA (FUNCIONA NO FREE PLAN)
date = "2023-08-12"

url = f"https://api.sportmonks.com/v3/football/fixtures/date/{date}"

params = {
    "api_token": API_TOKEN,
    "include": "league;participants",
}

response = requests.get(url, params=params)

print("STATUS:", response.status_code)
print("RESPONSE TEXT:")
print(response.text[:3000])
