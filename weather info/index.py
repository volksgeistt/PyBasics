import requests

city = input("Enter city name: ")
api_key = "your_api_key" # ( Add your OpenWaetherAPI Key )
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

res = requests.get(url).json()
print(f"{city}: {res['weather'][0]['description'].title()}, {res['main']['temp']}°C")
