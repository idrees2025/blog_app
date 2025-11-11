from django.test import TestCase
from blog_app.models import Blog
from django.urls import reverse
# Create your tests here.

class testtemplate(TestCase):
    def setUp(self):
        Blog.objects.create(title='this isa tile')

    def test_template_code(self):
        response=self.client.get(reverse('list'))
        self.assertEqual(response.status_code,200)

   