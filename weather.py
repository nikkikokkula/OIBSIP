import requests

# Take city name from user
city = input("Enter city name: ")

# Weather API key (replace with your own)
api_key = "Your_API_Key_Here"

# API URL
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

# Send request to API
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Check if city is found
if data["cod"] == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\nWeather Information")
    print("-------------------")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Weather Condition:", condition)
else:
    print("City not found")
