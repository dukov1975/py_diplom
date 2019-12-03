from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient


class TestAPI(APITestCase):

    def setUp(self):
        self.user = self.setup_user()
        self.client = APIClient()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        self.URL = 'http://127.0.0.1:8000/api/v1/'
        self.auth = {'Authorization': f'Token {self.token}'}

    @staticmethod
    def setup_user():
        return get_user_model().objects.create_user(
            email='garik@test.com',
            password='Test12345',
            type='shop',
            is_active=1,
            is_staff=1
        )
        return user

    # def test_register_user(self):
    #     method = '/api/v1/user/register'
    #     payload = {'first_name': 'имя ',
    #                'last_name': 'фамилия',
    #                'email': 'a.iskakov1989@gmail.com',
    #                'password': 'qwer1234A',
    #                'company': 'asdads',
    #                'position': '345345'}
    #     response = self.client.post(method, payload)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    def test_mail_confirm(self):
        method = f'{self.URL}user/register/confirm'
        payload = {'email': 'a.iskakov1989@gmail.com',
                   'token': '3abeab8e34a5'}
        response = self.client.post(method, payload, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact_add(self):
        method = '/api/v1/user/contact'
        payload = {'city': 'Almaty',
                   'street': 'Shashkin street 40',
                   'house': 'Apartament 28',
                   'structure': '123',
                   'building': '123',
                   'apartment': '123',
                   'phone': '+49564563242'}
        response = self.client.post(path=method, data=payload, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_contact_edit(self):
        method = '/api/v1/user/contact'
        payload = {'city': 'Almaty',
                   'street': 'Shashkin street 40',
                   'house': 'Apartament 28',
                   'structure': '1234',
                   'building': '123345',
                   'apartment': '123345',
                   'id': '1',
                   'phone': '+45465421654'}
        response = self.client.put(path=method, data=payload, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact_delete(self):
        method = '/api/v1/user/contact'
        payload = {'items': '5, 6, 4'}
        response = self.client.delete(path=method, data=payload, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_contacts_list(self):
        method = '/api/v1/user/contact'
        response = self.client.get(path=method, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop_list(self):
        method = '/api/v1/shops'
        response = self.client.get(path=method)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_list(self):
        method = '/api/v1/categories'
        response = self.client.get(path=method)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_detail(self):
        method = '/api/v1/user/details'
        payload = {'first_name': 'имя 545',
                   'last_name': 'фамилия54',
                   'email': 'a@a.ru11',
                   'password': 'qwer1234Aasd',
                   'company': '5345',
                   'position': '345345sdf'}
        response = self.client.get(path=method, data=payload, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)





