from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import time
from decimal import Decimal

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
def atr(request):
    request_atr = "https://api2.binance.com/api/v3/klines?symbol=" + "BTCUSDT" + "&interval=" + "4h" + "&limit=1000"
    response_atr = request_to_main_api(request_atr)
    data_atr = response_atr.json()
    # print(data)
    atr_ = Decimal(0.0)
    atr_pre = Decimal(max(Decimal(data_atr[1][2]) - Decimal(data_atr[1][3]),
                          Decimal(abs(Decimal(data_atr[1][2]) - Decimal(data_atr[1 - 1][4]))),
                          Decimal(abs(Decimal(data_atr[1][3]) - Decimal(data_atr[1 - 1][4])))))

    for i in range(2, len(data_atr) - 1):
        tr = Decimal(max(Decimal(data_atr[i][2]) - Decimal(data_atr[i][3]),
                         Decimal(abs(Decimal(data_atr[i][2]) - Decimal(data_atr[i - 1][4]))),
                         Decimal(abs(Decimal(data_atr[i][3]) - Decimal(data_atr[i - 1][4])))))
        atr_ = (atr_pre * 13 + tr) / 14
        atr_pre = atr_

    return Response({
        "message": atr_
    }, status=status.HTTP_200_OK)
