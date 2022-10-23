from django.test import TestCase, Client

from apps.users.models import User


class UserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.numbers_of_users = 5
        self.user_list = []

        self.valid_user_data = {
            'password': 'passuser',
            'username': 'usertest',
            'email': 'teste@test.com',
            'first_name': 'Test',
            'last_name': 'Test'
        }
        self.invalid_user_data = {
            'password': '',
            'username': '',
            'email': 'teste',
            'first_name': 'Test',
            'last_name': 'Test'
        }

        for i in range(1, self.numbers_of_users + 1):
            user = User.objects.create_user(
                username=f'usertest{i}',
                first_name='User',
                last_name=f'Test {i}',
                email=f'test{i}@test.com',
            )
            user.set_password(f'passuser{i}')
            user.save()
            self.user_list.append(user.username)
