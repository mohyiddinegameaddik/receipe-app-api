'''
    Tests for the Django admin modification
'''

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import client


class AdminSiteTests(TestCase):

