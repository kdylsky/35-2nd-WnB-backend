from django.db.models       import Q

from rooms.serializers      import RoomModelSerializer, RoomDetailSerializer

from rooms.models           import Room
from reservations.models    import Reservation  

class RoomRepo:
    def __init__(self) -> None:
        self.model           = Reservation
        self.model_room      = Room
        self.serializer      = RoomModelSerializer
        self.serializer_room = RoomDetailSerializer
    
    def check_room(self, q: tuple, check_in: str, check_out: str)-> object:
        reservations = []
        if check_in and check_out:
            reservations = self.model.objects.filter(
                Q(check_in__lte=check_in, check_out__gte=check_out)|
                Q(check_in__lte=check_in, check_out__gt=check_in)|
                Q(check_in__lt=check_out, check_out__gte=check_out)
            )
        rooms = Room.objects.filter(q).distinct().exclude(reservation__in=reservations)
        return rooms

    def get_list(self, rooms: object)-> dict:
        serializer = self.serializer(instance=rooms, many=True)
        return serializer.data

    def get_room_object(self, room_id: int)-> object:
        return self.model_room.objects.select_related('room_type', 'host', 'category')\
                               .prefetch_related('reservation_set', 'image_set', 'detailimage_set').get(id=room_id)

    def get_room(self, room_obj: int)-> dict:
        serializer = self.serializer_room(instance=room_obj)
        return serializer.data