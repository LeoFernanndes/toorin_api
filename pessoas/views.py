from rest_framework_simplejwt.views import TokenObtainPairView
from pessoas.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
