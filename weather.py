import requests
import json

WEATHER_API_KEY = '03efcb184462d78206348fdd558b8f21'

def get_local_weather(city_name):
    """ Gets the current weather based on the city """
    city = {'q': city_name, 'APPID': WEATHER_API_KEY}
    results = requests.get('http://api.openweathermap.org/data/2.5/weather?', params=city)
    return json.loads(results.text)

def serve_weather(city):
    """ Grabs what I want from the open weather api response """
    weather = get_local_weather(city)

    new_weather = {
        'temp': keltofah(weather['main']['temp']),
        'tempMin': keltofah(weather['main']['temp_min']),
        'tempMax': keltofah(weather['main']['temp_max']),
        'weather': weather['weather'][0]['description']
    }
    return new_weather

def keltofah(kel):
    """ Converts kelvin to fahrenheit """
    return (kel*9/5.0)-459.67
