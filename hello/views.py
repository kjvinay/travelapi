from django.shortcuts import render
from rest_framework import viewsets
from django.contrib import messages
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from django.db.models import F
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .serializers import areaSerializer,citySerializer,area_travelSerializer,city_travelSerializer
from .models import area,city,area_travel,city_travel

class areaView(viewsets.ModelViewSet):
    queryset = area.objects.all()
    serializer_class = areaSerializer

class cityView(viewsets.ModelViewSet):
    queryset = city.objects.all()
    serializer_class = citySerializer

class area_travelView(viewsets.ModelViewSet):
    queryset = area_travel.objects.all()
    serializer_class = area_travelSerializer



class city_travelView(viewsets.ModelViewSet):
      queryset = city_travel.objects.all()
      serializer_class = city_travelSerializer
      
    

               
