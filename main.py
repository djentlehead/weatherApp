import requests

# Insert your API key here. 
API_KEY = ''

def get_weather(city_name):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {description.capitalize()}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"City '{city_name}' not found. Please check the city name and try again.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
