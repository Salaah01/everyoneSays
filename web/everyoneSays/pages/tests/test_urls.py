"""Tests that the URLs route to the correct view."""

from unittest import TestCase
from django.urls import reverse, resolve
from ..views import index


class TestURLS(TestCase):
    """Tests that the URLs are routed to the correct view."""

    def test_index(self):
        """Test that the `index` url resolves the correct view."""
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
