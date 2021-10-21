from django.test import TestCase
from microblogs.forms import SignUpForm, PostForm
from microblogs.models import User, Post

class PostFormTestCase(TestCase):
    def setUp(self):
        self.form_input = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username': '@janedoe',
            'email': 'janedoe@example.org',
            'bio': 'My bio',
            'new_password': 'Password123',
            'password_confirmation': 'Password123'
        }
        self.post = {
            'author': self.form_input,
            'text': 'Wow, today was amazing'
        }

    def test_valid_post_form(self):
        self.form_post = {'text': 'That was terrible'}
        form = PostForm(data = self.form_post)
        self.assertTrue(form.is_valid())
