from django.shortcuts import render, HttpResponse
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')

class RegisterUserView(APIView):
    def post(self, requests):
        try:
            serializer = UserSerializer(data = requests.data)
            if not serializer.is_valid():
                return Response({"status": status.HTTP_403_FORBIDDEN, "errors": serializer.errors})
            serializer.save()
            return Response({"status": status.HTTP_201_CREATED, "message": "User Register Successfully"})
        except Exception as e:
            print(e)
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Something went Wrong"})