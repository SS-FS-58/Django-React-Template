from django.urls import path
from .views import UserSettingView

app_name = "user"

urlpatterns = [
    path('user_settings/', UserSettingView.as_view(), name="user_settings"),
]
