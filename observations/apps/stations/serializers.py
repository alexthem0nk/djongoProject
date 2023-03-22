from django.contrib.auth.models import User, Group
from rest_framework import serializers


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = stations
        fields = "__all__"
