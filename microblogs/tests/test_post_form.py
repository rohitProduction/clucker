from django.test import TestCase
from microblogs.forms import SignUpForm, PostForm
from microblogs.models import User, Post

class PostFormTestCase(TestCase):
    def setUp(self):
        self.form_post = {'text': 'That was terrible'}
        """self.post = {
            'author': self.form_input,
            'text': 'Wow, today was amazing'
        }"""

    def test_valid_post_form(self):
        form = PostForm(data = self.form_post)
        self.assertTrue(form.is_valid())

    def test_form_has_necessary_fields(self):
        form = PostForm()
        self.assertIn('text', form.fields)

    def test_form_uses_model_validation(self):
        self.form_post['text'] = 'x' * 281
        form = PostForm(data = self.form_post)
        self.assertFalse(form.is_valid())
