from rest_framework import viewsets
from rest_framework import filters
from .models import Subject
from .serializers import SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    resource_name = 'subjects'
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
