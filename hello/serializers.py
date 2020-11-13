from rest_framework import serializers
from datetime import datetime

from .models import area,city,area_travel,city_travel

class areaSerializer(serializers.ModelSerializer):
    class Meta:
        model = area
        fields = ('area_name', 'unique_id','at_longitude','at_latitude')
class citySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields = ( 'city_name', 'unique_id','at_longitude','at_latitude')
class area_travelSerializer(serializers.ModelSerializer):
    class Meta:
        model = area_travel
        fields = ('user_no', 'from_area_id','to_area_id','from_longitude','from_latitude','to_longitude','to_latitude','booking_time','online_booking','mobile_site_booking','car_cancellation','from_date','to_date','package_id','travel_type','vehicle_type')
class city_travelSerializer(serializers.ModelSerializer):
    class Meta:
        model = city_travel
        fields = ('user_no', 'from_city_id','to_city_id','from_longitude','from_latitude','to_longitude','to_latitude','booking_time','online_booking','mobile_site_booking','car_cancellation','from_date','to_date','package_id','travel_type','vehicle_type')
        
    def create(self, validated_data):
            return city_travel.objects.create(**validated_data)
        