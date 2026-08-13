from django.shortcuts import render
from django.http import HttpResponse
import requests
def index(request):
    return render(request, 'index.html')

def forcast(request):
    return render(request, 'forcast.html')

def climate(request):
    return render(request, 'climate_forcast_base.html')

def details(request):
    if request.method == "POST":
        city=request.POST['city']
        res=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid="API_ID"&units=metric"
        response=requests.get(res)
        forcast=response.json()
        return render(request, "climate_forcast_base.html", {"whether":forcast,"city": city})
    elif request.method == "GET":
        city = request.GET['city']
        res = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid="API_ID"&units=metric"
        response = requests.get(res)
        whether = response.json()
        return render(request, "forcast.html", {"forecast": whether, "city": city})
    else:
        return HttpResponse("<h1>Some thing went wrong</h1>")
