from django.urls    import path 

from rooms.views import RoomsView, RoomDetailView, get_room_list

urlpatterns = [
    path ('', RoomsView.as_view()),
    path('/<int:room_id>', RoomDetailView.as_view()),
    path("/test", get_room_list)
]