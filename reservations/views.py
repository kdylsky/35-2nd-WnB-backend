from django.http                import JsonResponse

from rest_framework             import status
from rest_framework.decorators  import parser_classes
from rest_framework.parsers     import JSONParser
from rest_framework.views       import APIView

from decorators.auth_handler      import login_decorators
from decorators.execption_handler import execption_hanlder
from reservations.serializers     import CreateReservationSchema
from reservations.service         import ReservationService


reservation_service = ReservationService()

class ReservationView(APIView):
    def post(self, request, *args, **kwargs):
        return post_reservation(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return get_reservation(request, *args, **kwargs)


class DetailReservationView(APIView):
    def get(self, request, *args, **kwargs):
        return get_detail_reservation(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return delete_detail_reservation(request, args, kwargs)


@parser_classes([JSONParser])
@execption_hanlder()
@login_decorators()
def post_reservation(request, *args, **kwargs):
    user   = request.user
    data   = request.data
    params = CreateReservationSchema(data=data)
    params.is_valid(raise_exception=True)
    return JsonResponse(reservation_service.create_reservation(user, **params.data), status=status.HTTP_201_CREATED)

@parser_classes([JSONParser])
@execption_hanlder()
@login_decorators()
def get_reservation(request, *args, **kwargs):
    user = request.user
    return JsonResponse(reservation_service.get_reservation_list(user), status=status.HTTP_200_OK, safe=False)

@parser_classes([JSONParser])
@execption_hanlder()
@login_decorators()
def get_detail_reservation(request, args, kwargs):
    user            = request.user
    reservation_id  = kwargs["reservation_id"] 
    return JsonResponse(reservation_service.get_detail_reservation_list(user, reservation_id), status=status.HTTP_200_OK)

@parser_classes([JSONParser])
@execption_hanlder()
@login_decorators()
def delete_detail_reservation(request, args, kwargs):
    user            = request.user
    reservation_id  = kwargs["reservation_id"] 
    return JsonResponse(reservation_service.delete_detail_reservation_list(user, reservation_id), status=status.HTTP_200_OK, safe=False)