from django.test import TestCase
from django.urls import reverse
from microblogs.models import User

class UserListViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('show_user', kwargs={'user_id': id})
