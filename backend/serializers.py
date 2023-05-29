from backend.models import LinkModel
from rest_framework import serializers


class LinkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkModel
        fields = ['long_link', 'short_link']
