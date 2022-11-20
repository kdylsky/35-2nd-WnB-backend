from django.urls            import path

from reservations.views     import  ReservationView

urlpatterns = [
    path("/test", ReservationView.as_view())
]