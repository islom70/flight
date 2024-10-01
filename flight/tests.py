from django.test import TestCase, Client
from flight.models import Flight


class FlightTest(TestCase):
    def setUp(self):
        self.client = Client(HTTP_X_API_KEY='secret')
        self.flight_data = {
            'flight_no': 'B737',
            'airline': 'Boeing',
            'departure_city': 'Tashkent',
            'arrival_city': 'New York',
            'departure_time': '2024-10-10T12:00:00Z',
            'arrival_time': '2024-10-11T14:00:00Z',
        }

    def test_save_flights(self):
        response = self.client.post('/api/v1/flights', self.flight_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_flights(self):
        Flight.objects.create(**self.flight_data)
        response = self.client.get('/api/v1/flights/B737')
        self.assertEqual(response.status_code, 200)