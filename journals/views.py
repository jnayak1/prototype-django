from rest_framework import viewsets
from rest_framework import filters
from .models import Journal
from .serializers import JournalSerializer


class JournalViewSet(viewsets.ModelViewSet):
    resource_name = 'journals'
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
