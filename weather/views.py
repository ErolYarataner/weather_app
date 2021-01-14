from django.shortcuts import render
import requests
from .models import City
# Create your views here.
def index(request):
    cities = City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=20c1238224c0c4f50dadbd66f77b4a1a'
    weather_data = []
    for city in cities:
        response = requests.get(url.format(city)).json()

        city_weather = {
            'city':city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data':weather_data}

    return render(request, 'weather/index.html', context)