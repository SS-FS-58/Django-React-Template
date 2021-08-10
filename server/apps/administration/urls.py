from django.urls import path

from .views import (test_send_email, test_notification)

app_name = "administration"

urlpatterns = [
    path('test_send_email/', test_send_email, name="test_send_email"),
    path('test_notification/', test_notification, name="test_notification"),
]
