from django.urls import path, include
from .views import index, register, RegisterUserView, login_page, LoginAPIView

urlpatterns = [
    path('', index, name="home"),
    path('register/', register, name="register"),
    path('login/', login_page, name="login"),
    path('api/v1/register/', RegisterUserView.as_view(), name="register_user"),
    path('api/v1/login/', LoginAPIView.as_view(), name="login_user"),
]