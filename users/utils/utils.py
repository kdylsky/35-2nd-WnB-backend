import re
import jwt
import bcrypt
from datetime import datetime

from django.conf import settings

from users.models       import User
from users.exceptions   import SignupRaiseError, CheckPasswordError

class AuthorProvider:
    def __init__(self):
        self.key = settings.JWT_KEY
        self.expire_sec = settings.JWT_EXPIRE_TIME
        self.refresh_expire_sec = settings.JWT_REFRESH_EXPIRE_TIME
    
    def hash_password(self, password: str)-> bool:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_request_password(self, password: str, user_password: str)-> bool:
        flag = bcrypt.checkpw(password.encode("utf-8"), user_password.encode("utf-8"))
        if not flag:
            raise CheckPasswordError
        return flag

    def create_token(self, user_id: int, is_expired = False)-> dict:
        exp = 0 if is_expired else self.get_curr_sec() + self.expire_sec
        token = jwt.encode({"user_id":user_id, "exp":exp}, self.key, algorithm="HS256")
        return {"access": token}

    def get_curr_sec(self)-> str:
        return datetime.now().timestamp()
    

author_provider= AuthorProvider()