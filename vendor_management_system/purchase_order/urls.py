from django.urls import path
from .views import POView,OnPOView

urlpatterns = [
    path('',POView.as_view()),
    path('<int:po_id>',OnPOView.as_view())
]