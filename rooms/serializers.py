from rest_framework import serializers
from rooms.models import Room, Image

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "url",


class RoomModelSerializer(serializers.ModelSerializer):
    image_set = ImageModelSerializer(many=True, read_only =True)
    class Meta:
        model = Room
        fields = "id", "name","price","address","longitude","bed", "description", "image_set"

# 위에 정의한 serialzer와 같다
# class RoomModelSerializer(serializers.ModelSerializer):
#     image = ImageModelSerializer(source="image_set", many=True, read_only =True)
#     class Meta:
#         model = Room
#         fields = "id", "name","price","address","longitude","bed", "description", "image"
