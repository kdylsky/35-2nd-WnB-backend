from rooms.repository import RoomRepo

class RoomService:
    def __init__(self) -> None:
        self.repo = RoomRepo()
    
    def get_list(self, q, check_in, check_out):
        rooms = self.repo.check_room(q, check_in, check_out)
        data  = self.repo.get_list(rooms)
        return data
