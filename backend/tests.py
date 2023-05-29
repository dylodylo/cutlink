from backend.models import LinkModel
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.utils import json


class TestLinkModelViews(TestCase):
    def setUp(self) -> None:
        self.factory = APIClient()

    def test_post(self):
        response = self.factory.post('', json.dumps({'long_link': 'https://google.com'}), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(LinkModel.objects.count(), 1)

    def test_get(self):
        instance = LinkModel.objects.create(long_link='https://yahoo.com')
        url = f'/{instance.short_link}'
        response = self.factory.get(url)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['long_link'], 'https://yahoo.com')
