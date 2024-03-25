from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework import status


class SignupViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("signup")

    def test_signup_success(self):
        data = {"username": "testuser", "password": "testpassword123"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], data["username"])
        self.assertTrue(Token.objects.filter(user__username=data["username"]).exists())

    def test_signup_fails_without_data(self):
        response = self.client.post(self.url, dict())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data,
            {
                "username": ["This field is required."],
                "password": ["This field is required."],
            },
        )

    def test_signup_fails_without_password(self):
        data = {"username": "testuser"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"password": ["This field is required."]})

    def test_signup_fails_without_username(self):
        data = {"password": "testpassword123"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"username": ["This field is required."]})

    def test_signup_fails_with_existing_username(self):
        data = {"username": "testuser", "password": "testpassword123"}
        self.client.post(self.url, data)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"username": ["A user with that username already exists."]}
        )
