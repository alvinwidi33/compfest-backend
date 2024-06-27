from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Reservation
from .serializers import ReservationGet, ReservationPost

@api_view(['GET'])
def get_list_reserve_all(request):
    reservation = Reservation.objects.all()
    serializer = ReservationGet(reservation, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_list_reserve_branch(request, branch):
    reservation = Reservation.objects.filter(branch=str(branch))
    serializer = ReservationGet(reservation, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_list_reserve_customer_history(request, name):
    reservation = Reservation.objects.filter(name=str(name))
    serializer = ReservationGet(reservation, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_list_reserve_customer(request, name):
    reservation = Reservation.objects.filter(name=str(name), is_done=False) 
    serializer = ReservationGet(reservation, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_reserve(request):
    serializer = ReservationPost(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_reserve(request, id):
    try:
        reservation = Reservation.objects.get(id=str(id))
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ReservationPost(reservation, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def done_reserve(request, id):
    try:
        reservation = Reservation.objects.get(id=str(id))
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ReservationPost(reservation, data=request.data, partial=True) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)