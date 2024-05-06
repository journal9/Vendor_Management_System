from django.urls import path
from .views import VendorView,OnVEndor

urlpatterns = [
    path('',VendorView.as_view()),
    path('<int:vendor_id>',OnVEndor.as_view())
]