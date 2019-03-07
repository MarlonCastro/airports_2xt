from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse

import requests
# Create your views here.


def first(request):
    response = requests.get('http://stub.2xt.com.br/air/airports/qrHvDHxyWvwmvlDqrHAJcmzcENtmvXmO', auth=('', ''))
    context = {'aiports': response.json()}
    return render(request, 'flights/first.html', context)

def index(request):
    return HttpResponse('index aqui')