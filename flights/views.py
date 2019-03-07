from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse

import requests
import json
# Create your views here.


def first(request):
    response = requests.get('http://stub.2xt.com.br/air/airports/qrHvDHxyWvwmvlDqrHAJcmzcENtmvXmO', auth=('', ''))
    context = {'aiports': response.json()}
    data = response.json()
    control = 0 
    controlI = 0
    #print(json.loads(data))
    for i, value in data.items():
      if control <= 5:
        for j, valueD in data.items():
          print(controlI)
          if controlI <= 5:
            if i != j:
              print("Compares "+ i +" com "+ j )
          else:
            controlI = 0
            break
        controlI += 1
      else:
        break
      control+= 1
       #print(returnDataflights(value))


    return render(request, 'flights/first.html', context)

def returnDataflights(data):
  text = data

  # response = requests.get('http://stub.2xt.com.br/air/search/qrHvDHxyWvwmvlDqrHAJcmzcENtmvXmO/{dAiport}/{aAiport}/2019-17-04', auth=('', ''))
  return text.city

def calculesGeneral():
  return ""

def index(request):
   return HttpResponse('ssss')