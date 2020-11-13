from django.urls import path,include 
from . import views
from rest_framework import routers
from .models import area,city,area_travel,city_travel


router = routers.DefaultRouter()
router.register('area', views.areaView)
router.register('city', views.cityView)
router.register('area_travel', views.area_travelView)
router.register('city_travel', views.city_travelView)

urlpatterns = [
    path('', include(router.urls)),
   ]