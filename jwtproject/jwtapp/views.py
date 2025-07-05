from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import Profile
from .permissions import IsOwner
from .serializers import ProfileSerializer
from .serializers import UserSerializer

def response_view(request):
    return HttpResponse("User response")


class HelloView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = {"message": "Hello world!"}
        return Response(content)


class UserList(generics.ListAPIView):
    """Show users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class UserDetail(generics.RetrieveAPIView):
    """Get a user details."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileList(generics.ListCreateAPIView):
    """Get or create profiles belonging to creating user."""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        """Associates creating user with user's profile."""
        serializer.save(owner=self.request.user)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """Get, change, or destroy a profile belonging to creating user."""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        resp = Response({
            "message": "This is a protected view.",
            "headers": self.request.headers,
        })
        return resp
