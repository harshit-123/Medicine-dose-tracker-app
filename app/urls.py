from django.urls import path, include
from .views import index, register, RegisterUserView

urlpatterns = [
    # path('register/', register, name="register"),
    path('api/v1/register/', RegisterUserView.as_view(), name="register_user"),
]