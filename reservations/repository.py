import uuid

from rooms.models             import Room
from reservations.models      import Reservation
from reservations.serializers import ReservationModelSerialzier, ReservationModelSchema, ReservationDetailSchema

class ReservationRepo:
    def __init__(self) -> None:
        self.model_room               = Room
        self.model_reservation        = Reservation
        self.serializer               = ReservationModelSerialzier
        self.serializer_schema        = ReservationModelSchema
        self.serializer_deatil_schema = ReservationDetailSchema

    def get_room_object(self, room_id: int)-> object:
        """ 아이디로 room객체 반환 """
        return self.model_room.objects.get(id=room_id)

    def create(self, user: object, room_object: object, check_in: str, check_out: str, people: int, price: float)-> dict:
        """ serializer로 reservation객체 생성 후 반환 """
        number  = str(uuid.uuid4())     
        data    = {
            "user"      : user.id,
            "room"      : room_object.id,
            "check_in"  : check_in,
            "check_out" : check_out,
            "people"    : people,
            "price"     : price,
            "number"    : number
        }
        serializer = self.serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
    
    def get_reservation_object_all(self, user: object)-> dict:
        """ user객체의 모든 reservation객체 반환 """
        return self.model_reservation.objects.filter(user=user)
    
    def get_reservation_all(self, reservation_objects: object)-> dict:
        """ serializer로 모든 reservation객체 반환 """
        serializer = self.serializer_schema(instance=reservation_objects, many=True)
        return serializer.data
    
    def get_reservation_object(self, user: object, reservation_id: int)-> object:
        """ user객체의 특정 reservation객체 반환"""
        return self.model_reservation.objects.get(id=reservation_id, user=user)

    def get_reservation(self, reservation_object: object)-> dict:
        """ serializer로 특정 reservation객체 반환 """
        serializer = self.serializer_deatil_schema(instance=reservation_object)
        return serializer.data
        