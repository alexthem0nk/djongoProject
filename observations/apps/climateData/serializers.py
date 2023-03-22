from django.contrib.auth.models import User, Group
from rest_framework import serializers


class climateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = climateData
        fields = "__all__"
