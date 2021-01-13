from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    city = 'Istanbul'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=20c1238224c0c4f50dadbd66f77b4a1a'

    response = requests.get(url.format(city))

    print(response.text)

    return render(request, 'weather/index.html')