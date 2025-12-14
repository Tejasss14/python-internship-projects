import requests

API_KEY = "5f63e42cf80468ee86cf622ebbc6014c"  

def get_weatherdata(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("City not found!")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed_ms = data["wind"]["speed"]
        wind_speed_kmh = wind_speed_ms * 3.6

        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
        print(f"Wind Speed: {wind_speed_kmh:.2f} km/h")

    except Exception as e:
        print("Error fetching data:", e)


city_name = input("Enter city name: ")
get_weatherdata(city_name)
