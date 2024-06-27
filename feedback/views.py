from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from feedback.models import Feedback
from feedback.serializers import FeedbackGet, FeedbackPost

@api_view(['GET'])
def get_feedback_name(request, name):
    feedback = Feedback.objects.filter(name=str(name))
    serializer = FeedbackGet(feedback, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_feedback_branch(request, branch):
    feedback = Feedback.objects.filter(branch=str(branch))
    serializer = FeedbackGet(feedback, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_list_feedback(request):
    feedback = Feedback.objects.all()
    serializer = FeedbackGet(feedback, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_feedback(request):
    serializer = FeedbackPost(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)