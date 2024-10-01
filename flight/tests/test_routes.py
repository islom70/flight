# app/tests/test_routes.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from flight.models import Flight


class FlightTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.api_key = 'secret'
        self.client.defaults['HTTP_X_API_KEY'] = self.api_key

    def test_create_flight(self):
        response = self.client.post('/api/v1/flights', {
            'flight_no': 'AI101',
            'airline': 'Air India',
            'departure_city': 'Delhi',
            'arrival_city': 'New York',
            'departure_time': '2024-09-19T10:00:00Z',
            'arrival_time': '2024-09-19T20:00:00Z'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['flight_no'], 'AI101')

    def test_create_flight_invalid_data(self):
        response = self.client.post('/api/v1/flights', {
            'flight_no': '',
            'airline': 12345,
            'departure_city': '',
            'arrival_city': 'New York',
            'departure_time': 'invalid_datetime',
            'arrival_time': '2024-09-19T08:00:00Z'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_flight(self):
        Flight.objects.create(
            flight_no='AI101',
            airline='Air India',
            departure_city='Delhi',
            arrival_city='New York',
            departure_time='2024-09-19T10:00:00Z',
            arrival_time='2024-09-19T20:00:00Z'
        )
        response = self.client.get('/api/v1/flights/AI101')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['flight_no'], 'AI101')

    def test_get_flight_not_found(self):
        response = self.client.get('/api/v1/flights/INVALID')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_api_key(self):
        self.client.defaults['HTTP_X_API_KEY'] = 'invalid_key'
        response = self.client.get('/api/v1/flights/AI101')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
