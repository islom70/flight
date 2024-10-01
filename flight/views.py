from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Flight
from flight.serializers import FlightSerializer


@api_view(['POST'])
def save_flight(request):
    serializer = FlightSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_flight(request, flight_no):
    try:
        flight = Flight.objects.get(flight_no=flight_no)
    except Flight.DoesNotExist:
        return Response({"error": "Flight not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = FlightSerializer(flight)
    return Response(serializer.data, status=status.HTTP_200_OK)



