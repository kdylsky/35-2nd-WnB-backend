from users.serializers import UserSerializer

class UserRepo:
    def __init__(self) -> None:
        self.serializer = UserSerializer

    def create(self, first_name, last_name, email, phone_number, birth_day, password):
        data = {
            "first_name"    : first_name,
            "last_name"     : last_name,
            "email"         : email,
            "phone_number"  : phone_number,
            "birth_day"     : birth_day,
            "password"      : password
        }
        user = self.serializer(data=data)
        user.is_valid(raise_exception=True)
        user.save()
        return user.data