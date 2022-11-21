from rest_framework      import serializers

from rooms.models        import Room, Image, Category, RoomType, DetailImage, Facility
from hosts.models        import Host
from reservations.models import Reservation

class ImageModelSerializer(serializers.ModelSerializer):
    """ 중첩 serializer를 위한 이미지 모델 serializer"""
    class Meta:
        model = Image
        fields = "url",


class RoomModelSerializer(serializers.ModelSerializer):
    """
    전체 room list 정보를 위한 serializer
    """
    image_set = ImageModelSerializer(many=True, read_only =True)
    class Meta:
        model = Room
        fields = "id", "name","price","address","longitude","bed", "description", "image_set"


class CategoryModelSerializer(serializers.ModelSerializer):
    """ 중첩 serializer를 위한 카테고리 모델 serializer"""
    class Meta:
        model = Category
        fields = "__all__"


class RoomTypeModelSerializer(serializers.ModelSerializer):
    """ 중첩 serializer를 위한 방타입 모델 serializer"""
    class Meta:
        model = RoomType
        fields = "__all__"


class HostModelSerializer(serializers.ModelSerializer):
    """ 중첩 serializer를 위한 호스트 모델 serializer"""
    class Meta:
        model = Host
        fields = "__all__"


class DetailImageModelSerializer(serializers.ModelSerializer):
    """ 중첩 serializer를 위한 상세이미지 모델 serializer"""
    class Meta:
        model = DetailImage
        fields = "url",


class FacilityModelSerializer(serializers.ModelSerializer):
    """ 중첩 serializer를 위한 편의시설 모델 serializer"""
    class Meta:
        model = Facility
        fields = "__all__"


class ReservationModelSerializer(serializers.ModelSerializer):
    """ 중첩 serializer를 위한 예약 모델 serializer"""
    class Meta:
        model = Reservation
        fields = "check_in","check_out"


class RoomDetailSerializer(serializers.ModelSerializer):
    """
    room detail 정보를 위한 serializer
    """
    category        = CategoryModelSerializer(read_only=True)
    room_type       = RoomTypeModelSerializer(read_only=True) 
    host            = HostModelSerializer(read_only=True)
    image_set       = ImageModelSerializer(read_only=True, many=True)
    detailimage_set = DetailImageModelSerializer(read_only=True, many=True)
    facilities      = FacilityModelSerializer(read_only=True, many=True)
    reservation_set = ReservationModelSerializer(read_only=True, many=True)
    
    class Meta:
        model = Room
        fields = "id", "name", "address", "detail_address", "price", "description", "longitude", "latitude", "maximum_occupancy",\
              "bedroom", "bathroom", "bed", "reservation_set", "host", "category", "room_type", "image_set", "detailimage_set" , "facilities" 
                