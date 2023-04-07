import requests

payload = {
    "company_name": "bokita",
    "logo_url": "/Users/Nacho/Desktop/VentureClub/assets/logoboca.png"
}

response = requests.post("http://127.0.0.1:5000/generate_image", json=payload)

print(response.status_code)
print(response.json())