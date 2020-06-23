from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import user
from .serializers import userserializer

# Create your views here.
class user_display(APIView):

    def get(self,request):
        user1 = user.objects.all()
        serializer = userserializer(user1,many = True)
        return Response(serializer.data)
    
    def post(self , request):
        pass