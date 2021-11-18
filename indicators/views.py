from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def test(request):

    return Response({
        "message": "just for test"
    }, status=status.HTTP_200_OK)
