from reservations.repository import ReservationRepo


class ReservationService:
    def __init__(self) -> None:
        self.repo = ReservationRepo()
    
    def create_reservation(self, user: object, room: int, check_in: str, check_out: str, people: int, price: float)-> dict:
        room_object = self.repo.get_room_object(room)
        data = self.repo.create(user, room_object, check_in, check_out, people, price)
        return data

    def get_reservation_list(self, user: object)-> dict:
        reservation_objects = self.repo.get_reservation_object_all(user)
        data = self.repo.get_reservation_all(reservation_objects)
        return data 
    
    def get_detail_reservation_list(self, user: object, reservation_id: int)-> dict:
        reservation_object = self.repo.get_reservation_object(user, reservation_id)
        data = self.repo.get_reservation(reservation_object)
        return data