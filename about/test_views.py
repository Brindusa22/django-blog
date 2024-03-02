from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


# Create your tests here.

class TestCollaborateForm(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(title="About Me", content="This is about me")
        self.about_content.save()

    def render_about_page_with_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me", response.content)
        self.assertIn(b"This is about me", response.content)
        self.assertIsInstance(response.context["collaborate_form"], CollaborateForm)