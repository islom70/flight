from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invalid_key = 'invalid_key'

    def test_missing_api_key(self):
        response = self.client.get('/api/v1/flights/AI101')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_invalid_api_key(self):
        self.client.defaults['HTTP_X_API_KEY'] = self.invalid_key
        response = self.client.get('/api/v1/flights/AI101')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
