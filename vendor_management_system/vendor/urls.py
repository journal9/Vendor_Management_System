from django.urls import path
from .views import Vendor,OnVEndor

urlpatterns = [
    path('',Vendor.as_view()),
    path('<int:vendor_id>',OnVEndor.as_view())
]