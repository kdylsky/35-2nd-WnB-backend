from django.urls    import path 

from rooms.views    import get_room_list, get_detail_room_view

urlpatterns = [
    path("", get_room_list),
    path("/<int:room_id>", get_detail_room_view)
]