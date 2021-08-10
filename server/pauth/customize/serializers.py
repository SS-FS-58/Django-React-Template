from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(PTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token
