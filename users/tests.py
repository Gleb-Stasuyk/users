from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


User = get_user_model()


class AccountTests(APITestCase):
    """
    Test cases for users CRUD operations 
    """

    def setUp(self) -> None:
        """
        Add 2 users and get token
        """
        self.user = User.objects.create_user(
            username='admin', password='passPASS!@#1')
        self.user2 = User.objects.create_user(
            username='user', password='passPASS!@#1')
        url = reverse('token_obtain_pair')
        data = {
            'username': 'admin',
            'password': 'passPASS!@#1',
        }
        response = self.client.post(url, data, format='json')
        self.token = response.data['access']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)


    def test_create_user(self) -> None:
        """
        Ensure we can create a new users.
        """
        url = reverse('user-list')
        data = {
            'username': 'admin2',
            'password': 'passPASS!@#1',
            'is_active': 'true'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(len(User.objects.all()), 3)


    def test_get_users_list(self) -> None:
        """
        Ensure we can get a users list.
        """
        url = reverse('user-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(User.objects.all()), 2)


    def test_get_second_user(self) -> None:
        """
        Ensure we can get user by id.
        """
        url = reverse('user-detail', args=[2])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'user')


    def test_put_second_user(self) -> None:
        """
        Ensure we can PUT user by id.
        """
        url = reverse('user-detail', args=[2])
        data = {
            'username': 'admin100500',
            'password': 'passPASS!@#1',
            'is_active': 'true',
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'admin100500')
        self.assertEqual(response.data['last_name'], 'Last Name')



    def test_destroy_user(self) -> None:
        """
        Ensure we can delete user by id.
        """
        url = reverse('user-detail', args=[2])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(User.objects.all()), 1)
