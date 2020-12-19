from .models import Site
from rest_framework import serializers


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['url', 'http_code', 'date', "ip_address", 'timeout']
