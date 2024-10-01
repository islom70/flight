from datetime import datetime

from rest_framework import serializers

from flight.models import Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['flight_no', 'airline', 'departure_city', 'arrival_city', 'departure_time', 'arrival_time']

    def validate_flight_no(self, value):
        if not value:
            raise serializers.ValidationError('Flight_No is required!')
        return value

    def validate_airline(self, value):
        if not value or not isinstance(value, str):
            raise serializers.ValidationError('Airline is required and must be a string!')
        return value

    def validate_departure_city(self, value):
        if not value or not isinstance(value, str):
            raise serializers.ValidationError('Departure_City is required and must be a string!')
        return value

    def validate_arrival_city(self, value):
        if not value or not isinstance(value, str):
            raise serializers.ValidationError('Arrival_City is required and must be a string!')

    def validate_departure_time(self, value):
        if not isinstance(value, datetime):
            raise serializers.ValidationError('Departure_Time must be a valid datetime!')
        return value

    def validate_arrival_time(self, value):
        if not isinstance(value, datetime):
            raise serializers.ValidationError('Arrival_Time must be a valid datetime!')
        return value

    def validate(self, data):
        if data['departure_time'] >= data['arrival_time']:
            raise serializers.ValidationError('Departure time must be before arrival time!')
