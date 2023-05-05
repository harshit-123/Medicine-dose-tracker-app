from django.shortcuts import render
from .serializers import UserSerializer, UserLoginSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')

class RegisterUserView(APIView):
    def post(self, requests):
        try:
            serializer = UserSerializer(data = requests.data)
            if not serializer.is_valid():
                return Response({"status": status.HTTP_403_FORBIDDEN, "errors": serializer.errors})
            serializer.save()
            # user = User.objects.get(email = serializer.data['email'])
            # token_obj, _ = Token.objects.get_or_create(user=user)  # used for Token Authentication
            # refresh = RefreshToken.for_user(user)
            return Response({
                "status": status.HTTP_201_CREATED, 
                "message": "User Register Successfully",
                "data": serializer.data,
                # 'refresh': str(refresh), 
                # 'access': str(refresh.access_token)
            })
        except Exception as e:
            # print(e)
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Something went Wrong"})
        
        
class LoginAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user_obj = User.objects.get(email = request.data['email'])
        if user_obj is None:
            return Response({"status": status.HTTP_404_NOT_FOUND, "message": "Check username and password"})
            
        refresh = RefreshToken.for_user(user_obj)
        return Response({"status": status.HTTP_200_OK, "message": "Login Successful", 'refresh': str(refresh),
        'access': str(refresh.access_token),})
        

    def get(self, request):
        user_objs = User.objects.all()
        serializer = UserSerializer(user_objs, many=True)
        return Response({'status': status.HTTP_200_OK, 'payload': serializer.data})
    
    def patch(self, request):
        try:
            user_obj = User.objects.get(email = request.data['email'])
            serializer = UserSerializer(user_obj, data = request.data, partial=True)
            if not serializer.is_valid():
                return Response({"status": status.HTTP_403_FORBIDDEN, "message": serializer.errors})
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "message": "User Updated Successfully"})
            
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request):
        try:
            user_obj = User.objects.get(email = request.data['email'])
            user_obj.delete()
            return Response({'status': status.HTTP_200_OK, 'message': 'User Deleted Successfully'})
        except Exception as e:
            return Response({"status": status.HTTP_403_FORBIDDEN, 'messgae': 'Invalid ID'})