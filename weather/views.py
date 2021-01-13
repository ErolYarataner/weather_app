from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    city = 'Berlin'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=20c1238224c0c4f50dadbd66f77b4a1a'

    response = requests.get(url.format(city)).json()

    city_weather = {
        'city':city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    context = {'city_weather':city_weather}

    return render(request, 'weather/index.html', context)