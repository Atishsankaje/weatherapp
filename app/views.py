from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    city=request.GET.get('city')
    api_key='ca1c5b81eca9e4bdc248208166093c7a'
    api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    print(api_url)
    api=requests.get(api_url).json()
    temperature=api['main']['temp']
    wind_speed = api['wind']['speed']
    humidity = api['main']['humidity']
    cityname=api['name']
    country=api['sys']['country']
    weather = api["weather"][0]['main']
    description = api['weather'][0]['description']
    icon = api['weather'][0]['icon']
    img_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    return render(request,'index.html',{'temperature':temperature, 'cityname':cityname, 'country':country, 'wind_speed':wind_speed, 'humidity':humidity, 'weather':weather, 'description':description, 'img_url':img_url})

