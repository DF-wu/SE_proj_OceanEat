
from OceanEat.models import *
from OceanEat.serializers import *
from rest_framework import viewsets

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
        '''
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
        '''
            try:
                user = models.User.objects.get(name = login_name)
                if user.password == login_password:
                    request.session['username'] = user.name
                    request.session['useremail'] = user.email
                    messages.add_message(request, messages.SUCCESS, '成功登入！')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, "密碼錯誤，請再檢查一次")
            except:
                messages.add_message(request, messages.WARNING, "找不此使用者")
        else:
            messages.add_message(request, messages.INFO, "請檢查輸入的欄位內容")
    else:
        login_form = forms.LoginForm()

    data={
       'state':True,
       'usr': login_password,
       'message':message
    }
    #returnValue = magicNum, message
    return HttpResponse(json.dumps(data))
    #return render(request, 'login.html', locals())

