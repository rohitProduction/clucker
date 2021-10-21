from django.test import TestCase
from django.urls import reverse
from microblogs.models import User

class UserListViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('user_list')

    def test_sign_up_url(self):
        self.assertEqual(self.url, '/users/')

    def test_correctly_listed_all_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_list.html')
        u_list = response.context['u_list']
        count = User.objects.count()
        self.assertEqual(len(u_list), count)
