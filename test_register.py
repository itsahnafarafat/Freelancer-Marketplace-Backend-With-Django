import requests

# ✅ Update this URL based on your actual endpoint path
url = "http://127.0.0.1:8000/api/register/"

# ✅ Data to send for registration
data = {
    "username": "johndoe",
    "email": "john@example.com",
    "password": "secure1234"
}

# ✅ Send the POST request
response = requests.post(url, json=data)

# ✅ Output the result
print("Status Code:", response.status_code)

try:
    print("Response Data:", response.json())
except Exception:
    print("Raw Response:", response.text)
