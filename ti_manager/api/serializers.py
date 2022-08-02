from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    # serializador para metodo post
    name = serializers.CharField(maxlength=200)
    email = serializers.EmailField()