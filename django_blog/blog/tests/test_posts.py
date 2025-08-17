from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='bob', password='testpass')
        self.post = Post.objects.create(title='Hello', content='World', author=self.user)

    def test_list_view(self):
        resp = self.client.get(reverse('post-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.post.title)

    def test_detail_view(self):
        resp = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.post.content)

    def test_create_requires_login(self):
        resp = self.client.get(reverse('post-create'))
        self.assertEqual(resp.status_code, 302)  # redirect to login

    def test_update_permission(self):
        other = User.objects.create_user(username='alice', password='pass')
        self.client.login(username='alice', password='pass')
        resp = self.client.get(reverse('post-update', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 403)  # forbidden for non-author