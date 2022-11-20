import uuid

from rooms.models import Room
from reservations.models      import Reservation
from reservations.serializers import ReservationModelSerialzier, ReservationModelSchema

class ReservationRepo:
    def __init__(self) -> None:
        self.model_room = Room
        self.model = Reservation
        self.serializer = ReservationModelSerialzier
        self.serializer_two = ReservationModelSchema
    
    def get_room_object(self, room_id: int)-> object:
        return self.model_room.objects.get(id=room_id)

    def create(self, user: object, room_object: object, check_in: str, check_out: str, people: int, price: float)-> dict:
        number = str(uuid.uuid4())     
        data = {
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
    
    def get_reservation_object(self, user: object)-> dict:
        return self.model.objects.filter(user=user)
    
    def get_reservation(self, reservation_objects: object)-> dict:
        serializer = self.serializer_two(instance=reservation_objects, many=True)
        return serializer.data