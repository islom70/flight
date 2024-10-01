from django.urls import path
from flight import views

urlpatterns = [
    path('flights/', views.save_flight, name='save_flight'),
    path('flights/<str:flight_no>/', views.get_flight, name='get_flight'),
]