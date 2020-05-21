"""Tests that the views are correctly rendered."""

from unittest import TestCase
from django.urls import reverse
from django.test import Client

class TestViews(TestCase):
    """Tests that the views are correctly rendered."""
    
    def setUp(self):
        """Test set up."""
        self.client = Client()
    
    def test_index(self):
        """Test that the `index` view renders correctly."""
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)