from django.urls            import path

from reservations.views     import  ReservationView, DetailReservationView

urlpatterns = [
    path("", ReservationView.as_view()),
    path("/<int:reservation_id>", DetailReservationView.as_view())
]