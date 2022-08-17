from django.shortcuts import render
#--------- ViewSet import ------------------
from rest_framework import viewsets 
from django.shortcuts import get_object_or_404

from rest_framework import generics, status 
from rest_framework.request import Request 

from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D


from rest_framework import status

from rest_framework.views import APIView
    
#=========== Using of API View ==================
class RestaurantAPIView(APIView):
    def get(self,request):
        loc = Point(request.lng, request.lat)

        restaurants=Restaurant.objects.filter(point__distance_lte=(loc, D(m=3000)))

        serializer=views.RestaurantSerializer(restaurants,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=views.RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    