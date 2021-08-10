from django.conf import settings
from django.contrib.auth.models import User
from notifications.signals import notify
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .models import Auth_Level
from .service.email import Email


# Sample API parameters: to: "to@gmail.com", subject: "Subject", message: "Message of Email"
@api_view(['POST'])
def test_send_email(request):
    defaultFromEmail = settings.DEFAULT_FROM_EMAIL

    toEmail = request.data.get('to', '')
    subject = request.data.get('subject', '')
    message = request.data.get('message', '')

    sendMail = Email(defaultFromEmail, subject, message)

    if sendMail.verifyEmail(toEmail):
        if sendMail.sendSingleEmail(toEmail):
            response_data = {"success": True}
            return Response(data=response_data, status=status.HTTP_200_OK)
        else:
            return Response({'status': status.HTTP_403_FORBIDDEN,
                            'message': 'Faild to send email'},
                            status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Sample API parameters: to: "to@gmail.com", subject: "Subject", message: "Message of Notification"
@api_view(['POST'])
def test_notification(request):
    toEmail = request.data.get('to', '')
    subject = request.data.get('subject', '')
    message = request.data.get('message', '')

    user = User.objects.filter(email=toEmail).first()

    if user:
        notify.send(user, recipient=user, verb=subject, description=message)

    response_data = {"success": request.user.is_authenticated}
    return Response(data=response_data, status=status.HTTP_200_OK)
