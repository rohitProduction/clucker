from django.test import TestCase
from microblogs.models import User
from microblogs.models import Post
from django.core.exceptions import ValidationError

class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            password='Password123',
            bio='The quick brown fox jumps over the lazy dog.'
        )
        self.post = Post(author = self.user, text = "Wow", created_at = "2016-09-21")

    def test_valid_post(self):
        self._assert_post_is_valid()

    def test_text_can_be_280_characters_long(self):
        self.post.text = 'x' * 280
        self._assert_post_is_valid()

    def test_text_cannot_be_more_than_280_characters_long(self):
        self.post.text = 'x' * 281
        self._assert_post_is_invalid()

    def test_author_cannot_be_blank(self):
        self.post.author = None
        self._assert_post_is_invalid()

    def test_post_deleted_when_author_is_deleted(self):
        self.user.delete()
        self._assert_post_is_invalid()

    def test_user_may_author_multiple_posts(self):
        post2 = Post(author = self.user, text = "OMG", created_at = "2016-09-21")
        try:
            post2.full_clean()
        except (ValidationError):
            self.fail('Test post should be valid')
        self._assert_post_is_valid()

    def _assert_post_is_valid(self):
        try:
            self.post.full_clean()
        except (ValidationError):
            self.fail('Test post should be valid')

    def _assert_post_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.post.full_clean()
