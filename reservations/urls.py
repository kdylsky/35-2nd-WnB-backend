from django.urls            import path

from reservations.views     import  ReservationView, DetailReservationView

urlpatterns = [
    path("/test", ReservationView.as_view()),
    path("/test/<int:reservation_id>", DetailReservationView.as_view())
]