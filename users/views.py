from django.http                import JsonResponse

from rest_framework             import status
from rest_framework.parsers     import JSONParser
from rest_framework.decorators  import parser_classes, api_view

from users.service                import UserService
from users.serializers            import UserSerializer, LoginSerializer
from decorators.execption_handler import execption_hanlder

user_service = UserService()

@api_view(["POST"])
@parser_classes([JSONParser])
@execption_hanlder()
def signup(request, *args, **kwargs):
    data   = request.data
    params = UserSerializer(data=data)
    params.is_valid(raise_exception=True)
    return JsonResponse(user_service.signup(**params.data), status=status.HTTP_201_CREATED)

@api_view(["POST"])
@parser_classes([JSONParser])
@execption_hanlder()
def login(request, *args, **kwargs):
    data   = request.data
    params = LoginSerializer(data=data)
    params.is_valid(raise_exception=True)
    return JsonResponse(user_service.login(**params.data), status=status.HTTP_200_OK)

