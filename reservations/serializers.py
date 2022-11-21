from rest_framework      import serializers
from reservations.models import Reservation
from rooms.serializers   import ImageModelSerializer

class CreateReservationSchema(serializers.Serializer):
    """
    reservation객체 생성 시 요청 파라미터
    """
    room        = serializers.IntegerField()
    check_in    = serializers.DateField()
    check_out   = serializers.DateField()
    people      = serializers.IntegerField()
    price       = serializers.DecimalField(max_digits = 10, decimal_places = 2)

class ReservationModelSerialzier(serializers.ModelSerializer):
    """
    reservation모델 serializer
    """
    class Meta:
        model  = Reservation
        fields = "__all__"


class ReservationModelSchema(serializers.ModelSerializer):
    """
    reservation모델 역참조 포함 serializer
    """
    room            = serializers.PrimaryKeyRelatedField(source="room.name", read_only=True)
    address         = serializers.PrimaryKeyRelatedField(source="room.address", read_only=True)
    detail_address  = serializers.PrimaryKeyRelatedField(source="room.detail_address", read_only=True)
    image           = ImageModelSerializer(source="room.image_set", many=True, read_only =True)

    class Meta:
        model  = Reservation
        fields = "number", "check_in", "check_out", "room", "address", "detail_address", "image"