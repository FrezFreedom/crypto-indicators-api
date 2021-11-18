from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import time


def request_to_main_api(request_text):
    while True:
        try:
            response__ = requests.get(request_text)
            return response__
        except Exception as error:
            print("Main api can't response, in line 15 error is: " + str(error))
            print("Bot will go sleep for 10 seconds!")
            time.sleep(10)


@api_view(['POST'])
def test(request):

    return Response({
        "message": "just for test"
    }, status=status.HTTP_200_OK)
