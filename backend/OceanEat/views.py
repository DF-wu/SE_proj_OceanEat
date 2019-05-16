
from OceanEat.models import *
from OceanEat.serializers import *
from rest_framework import viewsets
import json
from django.contrib.sessions.models import Session
from django.http import HttpResponse, JsonResponse
from email.mime.text import MIMEText

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DishesViewSet(viewsets.ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def login(request):
    message = "Welcome"
    state = False
    if request.method == 'POST':
        
        login_password = "00"
        login_form = forms.LoginForm(request.POST)
        #if login_form.is_valid() or True:
        if True:
            obj = json.loads(request.body.decode('UTF-8'))
            login_name = obj['username']
            login_password = obj['password']
            #return HttpResponse(login_password)
            #message = "(" + username + ") 登入成功"
            try:
                user = models.User.objects.get(name = login_name)
                if user.password == login_password:
                    request.session['username'] = user.name
                    request.session['useremail'] = user.email
                    message = '成功登入！'
                    state = True
                    return redirect('/')
                else:
                    message = "密碼錯誤，請再檢查一次"
                    state = False
            except:
                message = "找不此使用者"
                state = False
        else:
            messages = "請檢查輸入的欄位內容"
            state = False
    else:
        login_form = forms.LoginForm()

    data={
       'state':state,
       'usr': login_password,
       'message':str(messages),
    }
    #returnValue = magicNum, message
    return HttpResponse(json.dumps(data))
    #return render(request, 'login.html', locals())

