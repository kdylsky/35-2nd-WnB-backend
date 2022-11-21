from rooms.repository import RoomRepo

class RoomService:
    def __init__(self) -> None:
        self.repo = RoomRepo()
    
    def get_list(self, q: tuple, check_in: str, check_out: str):
        rooms = self.repo.check_room(q, check_in, check_out)
        data  = self.repo.get_list(rooms)
        return data

    def get_detail_list(self, room_id: int):
        room_obj = self.repo.get_room_object(room_id)
        data     = self.repo.get_room(room_obj)
        return data