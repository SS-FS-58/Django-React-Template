import re

from django.core.mail import BadHeaderError, send_mail, send_mass_mail


class Email:
    fromEmail = None
    subject = None
    message = None

    def __init__(self, fromEmail, subject, message):
        self.fromEmail = fromEmail
        self.subject = subject
        self.message = message

    def verifyEmail(self, email):
        regex = "^\\w+([\\.-]?\\w+)*@\\w+([\\.-]?\\w+)*(\\.\\w{2,3})+$"

        if re.search(regex, email):
            return True
        else:
            return False

    def sendSingleEmail(self, email):
        try:
            if send_mail(self.subject, self.message, self.fromEmail, [email], fail_silently=False) == 0:
                return False
            return True
        except BadHeaderError:
            return False

    def sendEmailToUsers(self, users):
        recievers = []
        for user in users:
            recievers.append(user.email)

        try:
            if send_mail(self.subject, self.message, self.fromEmail, recievers, fail_silently=False) == 0:
                return False
            return True
        except BadHeaderError:
            return False

    def sendMassiveEmail(self, messages):
        try:
            if send_mass_mail(messages, fail_silently=False) == 0:
                return False
            return True
        except BadHeaderError:
            return False
