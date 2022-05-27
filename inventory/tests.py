from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Asset
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

class InventoryTest(APITestCase):
    def setUp(self):
        Asset.objects.create(asset_name='Chair', asset_price='399', depreciation_percent=12)

    def test_inventory(self):
        obj1 = Asset.objects.get(asset_name='Chair')
        self.assertEqual(obj1.asset_name, 'Chair')


