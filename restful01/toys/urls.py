from django.urls import path
from toys import views as toys_views

urlpatterns = [
    path('toys/', toys_views.ToyList.as_view()),
    path('toys/<int:pk>', toys_views.ToyDetail.as_view()),
]