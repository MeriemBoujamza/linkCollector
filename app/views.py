from django.shortcuts import render, HttpResponseRedirect
from bs4 import BeautifulSoup as bs
import requests
from .models import Link
# Create your views here.

def home(request):
    
    if request.method == 'POST':
        RequestedLink = request.POST.get('link','')

        response = requests.get(RequestedLink)
        soup = bs(response.text, 'html.parser')
    

        for link in soup.find_all('a'):
            link_address= link.get('href')
            name = link.string
            Link.objects.create(name=name,url=link_address)
        return HttpResponseRedirect('/')
    else: 
        data = Link.objects.all()   
        context = {
            'data': data,
        }
    return render(request,"base.html",context)


def clear(request):
    Link.objects.all().delete()
    return render(request,"base.html")