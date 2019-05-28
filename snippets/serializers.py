from rest_framework import serializers
from .models import *


class SnippetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ('__all__')
