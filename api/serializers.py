from rest_framework import serializers
from .models import Texts
# Model Serializers

class TextsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    class Meta:
        model = Texts
        fields = ['text1', 'text2']
