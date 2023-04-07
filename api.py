import requests

payload = {
    "company_name": "river",
    "logo_url": "/Users/Nacho/Desktop/VentureClub/assets/logoboca.png"
} 

response = requests.post("http://127.0.0.1:5000/receive_data", json=payload)

print(response.status_code)
print(response.json())