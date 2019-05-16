from django.shortcuts import render

from rest_framework.decorators import list_route
from rest_framework import viewsets, status
from rest_framework.response import Response
from PriceCount.models import PriceCount
from PriceCount.serializers import PriceCountSerializers
import  math


class CountOrderPrice(viewsets.ModelViewSet):
    queryset = PriceCount.objects.all()
    serializer_class = PriceCountSerializers
    # /api/PriceCount/countPrice/?foodprice=100&distance=1.3
    @list_route(methods=['get'])
    def countPrice(self,request):
        FoodPriceSum = request.query_params.get('foodprice', None)
        FoodPriceSum =  int(FoodPriceSum)

        distance = request.query_params.get('distance', None)
        distance = float(distance)
        BasePrice = 33
        OE_coef =1.0813
        DisC = 0
        ItemC = math.log10(FoodPriceSum)
        if distance < 1:
            DisC = 1
        else:
            DisC = 1.1 * distance

        orderprice = BasePrice * pow(OE_coef , DisC * ItemC )

        return Response(orderprice , status=status.HTTP_200_OK)
#         DisC = OE_ReLU(x) = 1 if x < 1 else 1.1x, where x = distance(KM)
#   + ItemC = Log10(x), where x = items total price


