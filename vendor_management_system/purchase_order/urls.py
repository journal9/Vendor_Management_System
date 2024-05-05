from django.urls import path
from .views import Order,OnOrderr

urlpatterns = [
    path('',Order.as_view()),
    path('<int:po_id>',OnOrderr.as_view())
]