from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )
    
    def test_post_title(self):
        self.assertEqual(self.post.title, 'Test Post')
    
    def test_post_content(self):
        self.assertEqual(self.post.content, 'This is a test post.')
    
    def test_post_author(self):
        self.assertEqual(self.post.author, self.user)
