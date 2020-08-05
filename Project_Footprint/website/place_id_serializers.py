from rest_framework import serializers
from .models import Place


class PlaceIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['naver_place_id']