import random
import string

from django.db import models


class LinkModel(models.Model):
    id = models.AutoField(primary_key=True)
    short_link = models.CharField(max_length=64, null=True)
    long_link = models.CharField(max_length=1024)

    @staticmethod
    def _create_short_link():
        characters = string.ascii_letters + string.digits
        while True:
            short_url = ''.join(random.choice(characters) for _ in range(6))
            if short_url not in LinkModel.objects.all().values_list('long_link', flat=True):
                return short_url

    @staticmethod
    def get_long_link(short_link):
        link_model = LinkModel.objects.get(short_link, )
        return link_model.long_link

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.short_link = self._create_short_link()
        super().save()


