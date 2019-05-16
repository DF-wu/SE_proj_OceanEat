from OceanEat.models import *
from OceanEat.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import list_route

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, **kwargs):
        users = Customer.objects.all()
        serializer = CustomerSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @list_route(methods=['post'])
    def create_customer(self, req):
        uid = Customer.objects.count()
        keys = """mail_address psw user_name nick_name gender phone_number address discribe other_contact custumer_rank custumer_rank_times delivery_mode""".split(' ')
        obj = dict()
        obj['customer_id'] = str(uid)
        for k in keys:
            s = req.data.get(k, None)
            if s: obj[k] = s
        c = Customer(**obj)
        c.save()
        return Response('ok', status=status.HTTP_200_OK)


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

    @list_route(methods=['post'])
    def create_delivery(self, req):
        uid = Customer.objects.count()
        keys = """mail_address psw user_name nick_name gender phone_number address discribe other_contact custumer_rank custumer_rank_times delivery_mode""".split(' ')
        obj = dict()
        obj['customer_id'] = str(uid)
        for k in keys:
            s = req.data.get(k, None)
            if s: obj[k] = s
        c = Customer(**obj)
        c.save()
        
        keys = """delivery_rank delivery_rank_time""".split(' ')
        obj = dict()
        obj['delivery_staff_id_id'] = str(uid)

        for k in keys:
            s = req.data.get(k, None)
            if s: obj[k] = s
        c = Delivery(**obj)
        c.save()
        return Response('ok', status=status.HTTP_200_OK)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DishesViewSet(viewsets.ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer