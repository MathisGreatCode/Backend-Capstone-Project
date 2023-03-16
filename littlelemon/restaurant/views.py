from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from .serializers import MenuItemSerializer, BookingSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import MenuItem, Booking

# Create your views here.


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]