import json
import uuid

from django.http            import JsonResponse
from django.views           import View

from reservations.models    import Reservation
from rooms.models           import Room
# from core.utils             import signin_decorator

from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import JsonResponse

from decorators.auth_handler import login_decorators
from decorators.execption_handler import execption_hanlder

from reservations.serializers import CreateReservationSchema
from reservations.service import ReservationService


reservation_service = ReservationService()

class ReservationView(APIView):
    def post(self, request, *args, **kwargs):
        return post_reservation(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return get_reservation(request, *args, **kwargs)

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


# class DetailReservationView(View):
#     # @signin_decorator
#     def get(self, request, reservation_number):
#         reservation          = Reservation.objects.select_related("room") \
#                                                   .prefetch_related("room__image_set") \
#                                                   .get(user = request.user, number = reservation_number)

#         result = {
#             'reservation_number'            : reservation.number,
#             'user_name'                     : reservation.user.last_name + " " + reservation.user.first_name,
#             'room'                          : reservation.room.name,
#             'price'                         : reservation.price,
#             'people'                        : reservation.people,
#             'check_in'                      : reservation.check_in,
#             'check_out'                     : reservation.check_out,
#             'images'                        : [image.url for image in reservation.room.image_set.all()],
#             'description'                   : reservation.room.description,
#             'address'                       : reservation.room.address + " " + reservation.room.detail_address,
#             'latitude'                      : reservation.room.latitude,
#             'longitude'                     : reservation.room.longitude
#         }
#         return JsonResponse({"RESULT": result}, status=200)
    
#     # @signin_decorator
#     def delete(self, request, reservation_number):
#         try:
#             Reservation.objects.get(user= request.user, number=reservation_number).delete()

#             return JsonResponse({'MESSAGE': 'RESERVATION_CANCEL'}, status=200)

#         except Reservation.DoesNotExist:
#             return JsonResponse({'MESSAGE': 'DOESNOT_EXIST_RESERVATION'}, status=400)
