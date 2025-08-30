
import requests

API_KEY = "d6cbde963b663d801edaa63f65e43669" 

city = input("Enter a city name: ")

base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    print(f"Fetching weather data for {city}...")
    response = requests.get(base_url)
    weather_data = response.json()

    main_data = weather_data['main']
    temperature = main_data['temp']
    humidity = main_data['humidity']

    weather_info = weather_data['weather'][0]
    description = weather_info['description']

    print(f"\n--- Weather in {city.title()} ---")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {description.title()}")

except:
    print(f"\nSorry, could not find weather data for '{city}'.")
    print("Please check the spelling or that the API key is active and correct.")