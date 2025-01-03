from django.shortcuts import render
from django.http import JsonResponse
import requests

import math
from datetime import datetime  # Correctly importing datetime class

# Create your views here.
def index(request):
    city_name = 'Kochi'
    if request.method=='POST':
        city_name=request.POST['city']
    
    
    
    
    
    

    # API call to OpenWeatherMap
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=360e4bc3865e745ec844bd7ec054ca11'

    # Fetching data
    response = requests.get(url)
    weather_data = response.json()

    # Convert timestamps to datetime objects
    sunrise_time = datetime.fromtimestamp(weather_data['sys']['sunrise'])
    sunset_time = datetime.fromtimestamp(weather_data['sys']['sunset'])
    current_time = datetime.fromtimestamp(weather_data['dt'])  # Current timestamp

    # Get the day from the current time
    day = current_time.strftime('%A')  # Returns the full day name (e.g., "Monday")

   # Get date and 3-letter month
    date_month = current_time.strftime('%d %b')
    # Preparing data to pass to the template
    
    data = {
        'city': city_name,
        'weather_description': weather_data['weather'][0]['description'],
        'temperature_kelvin': weather_data['main']['temp'],
        'temperature_celsius': math.floor(weather_data['main']['temp'] - 273.15),  # Convert to Celsius
        'humidity': weather_data['main']['humidity'],
        'temp_min_celsius': math.floor(weather_data['main']['temp_min'] - 273.15),  # Convert to Celsius
        'temp_max_celsius': math.floor(weather_data['main']['temp_max'] - 273.15),  # Convert to Celsius
        'sunrise': sunrise_time.strftime('%H:%M:%S'),
        'sunset': sunset_time.strftime('%H:%M:%S'),
        'visibility': math.floor(weather_data['visibility'] / 1000),  # Convert meters to kilometers
        'cloud': weather_data['clouds']['all'],
        'wind': weather_data['wind']['speed'],
        'pressure': math.floor((weather_data['main']['pressure'] / 1013.25) * 100),  # Convert to hPa
        'feel_temp': math.floor(weather_data['main']['feels_like'] - 273.15),  # Convert to Celsius
        'sea_level': weather_data['main'].get('sea_level', 'N/A'),  # Check for missing data
        'grnd_level': weather_data['main'].get('grnd_level', 'N/A'),  # Check for missing data
        'day': day,  # Add the day to the data dictionary
        'date_month': date_month,  # Add the date with 3-letter month to the data dictionary
    }

    return render(request, 'index.html', {'data': data})


def jsonres(request):
    data={
        "name":"Jerin",
        "age":21,
        "isactive":True,
    }
    return JsonResponse(data)