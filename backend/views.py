from backend.models import LinkModel
from backend.serializers import LinkModelSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView


class LinkModelRedirectView(RetrieveAPIView):
    serializer_class = LinkModelSerializer

    def get_object(self):
        short_link = self.kwargs['short_link']
        return get_object_or_404(LinkModel, short_link=short_link)


class LinkCreateModelView(CreateAPIView):
    queryset = LinkModel.objects.all()
    serializer_class = LinkModelSerializer
