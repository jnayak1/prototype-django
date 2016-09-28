from rest_framework_json_api import serializers
from .models import Journal


class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
