import requests

# gets ISS location
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

# gets the longitude and latitude of the ISS
data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (latitude, longitude)
print(f"ISS is currently at - {iss_position}")
print()


# Function to print out kanye quotes
def get_quote():
    response2 = requests.get(url="https://api.kanye.rest")
    response2.raise_for_status()

    kanye_quote = response2.json()
    each_quotes = kanye_quote["quote"]
    print(f"{each_quotes} - Kanye West")


get_quote()
