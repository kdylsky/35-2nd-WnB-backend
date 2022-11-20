from users.repository import UserRepo
from users.utils.utils import author_provider

class UserService:
    def __init__(self) -> None:
        self.repo = UserRepo()
    
    def signup(self, first_name, last_name, email, phone_number, birth_day, password):
        hashed_password = author_provider.hash_password(password)
        created_user = self.repo.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            birth_day=birth_day,
            password = hashed_password
        )
        return created_user
    
    def login(self, email, password):
        user = self.repo.get_user(email)
        author_provider.check_request_password(password,user.password)
        token = author_provider.create_token(user.id)
        return token