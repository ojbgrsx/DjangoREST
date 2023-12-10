import requests

URL = f"http://localhost:8080/people"
data = {"name": "Ayana", "age": 21, "email": "ayana12q34@gmail.com"}

r = requests.post(url=URL,json=data);

resp = requests.get(url=URL)

print(r.json())
for i in resp.json():
    print(i)
