from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Branch
from .serializers import BranchSerializer

@api_view(['POST'])
def add_branch(request):
    serializer = BranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_branch(request, id):
    try:
        branch = Branch.objects.get(id=id)
    except Branch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BranchSerializer(branch, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_list_branch(request):
    branch = Branch.objects.all()
    serializer = BranchSerializer(branch, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_branch_detail(request, id):
    try:
        branch = Branch.objects.get(id=id)
    except Branch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BranchSerializer(branch)
    return Response(serializer.data, status=status.HTTP_200_OK)
