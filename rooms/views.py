from django.http                import JsonResponse

from rest_framework             import status
from rest_framework.parsers     import JSONParser
from rest_framework.decorators  import api_view, parser_classes

from rooms.service                import RoomService
from rooms.utils.utils            import rooms_filter 
from decorators.execption_handler import execption_hanlder

room_service = RoomService()

@api_view(["GET"])
@parser_classes([JSONParser])
@execption_hanlder()
def get_room_list(request, *args, **kwargs):    
    filter_value = {
        "category"          : request.GET.get('category', None),
        "maximum_occupancy" : request.GET.get('maximum_occupancy', None),
        "bed"               : request.GET.get('bed', None),
        "bathroom"          : request.GET.get('bathroom', None),
        "bedroom"           : request.GET.get('bedroom', None),
        "address"           : request.GET.get('address',None),
        "room_type_ids"     : request.GET.getlist('room_type_id', None),
        "facility_ids"      : request.GET.getlist('facility_id', None),
        "min_price"         : request.GET.get('min_price', None),
        "max_price"         : request.GET.get('max_price', None),
    }
    check_in    = request.GET.get('check_in', None)
    check_out   = request.GET.get('check_out', None)
    q           = rooms_filter(filter_value)
    return JsonResponse(room_service.get_list(q, check_in, check_out), status=status.HTTP_200_OK, safe=False)

@api_view(["GET"])
@parser_classes([JSONParser])
@execption_hanlder()
def get_detail_room_view(request, *args, **kwargs):
    room_id = kwargs["room_id"]
    return JsonResponse(room_service.get_detail_list(room_id), status=status.HTTP_200_OK)