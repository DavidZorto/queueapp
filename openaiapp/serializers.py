from rest_framework import serializers
from .models import OpenAIResponse

class OpenAIResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenAIResponse
        fields = '__all__'