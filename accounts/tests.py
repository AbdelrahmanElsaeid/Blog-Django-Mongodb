from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import User
from rest_framework.authtoken.models import Token

# Create your tests here. 

class RegisterViewTests(APITestCase):

    
    def test_register(self):
        data={
            'username': "testemail",
            'email':"testemail@gmail.com",
            'password':"password##12345",
            'password2':"password##12345",

        }
        response = self.client.post(reverse('register'), data)    
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LoginLogoutViewTests(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='test',email="test@gmail.com", password="password##12345")
        self.token = Token.objects.create(user=self.user)

    def test_login(self):
        data = {
            'email':"test@gmail.com",
            'password':'password##12345',
            }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username="test")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) 
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)   

