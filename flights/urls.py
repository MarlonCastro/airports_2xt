from django.urls import path

from . import views

app_name = 'flights'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('first-step/', views.first, name='first'),
    # ex: /polls/5/results/
    # path('second-step/', views.second, name='second'),
    # ex: /polls/5/vote/

]