from django.db.models import Q
from reservations.models import Reservation  
from rooms.models import Room
from rooms.serializers import RoomModelSerializer

class RoomRepo:
    def __init__(self) -> None:
        self.model = Reservation
        self.model_room = Room
        self.serializer = RoomModelSerializer

    def check_room(self, q, check_in, check_out):
        reservations = []
        if check_in and check_out:
            reservations = self.model.objects.filter(
                Q(check_in__lte=check_in, check_out__gte=check_out)|
                Q(check_in__lte=check_in, check_out__gt=check_in)|
                Q(check_in__lt=check_out, check_out__gte=check_out)
            )
        rooms = Room.objects.filter(q).distinct().exclude(reservation__in=reservations)
        return rooms

    def get_list(self, rooms):
        serializer = self.serializer(instance=rooms, many=True)
        return serializer.data
