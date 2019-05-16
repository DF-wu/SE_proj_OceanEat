from django.db import models
from django_mysql.models import JSONField

class Customer(models.Model):
    customer_id = models.CharField(max_length=40, primary_key=True)
    mail_address = models.CharField(max_length=150)
    psw = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10, null=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=250, null=True)
    discribe = models.TextField(null=True)
    other_contact = models.TextField(null=True)
    custumer_rank = models.IntegerField(null=True, default=0)
    custumer_rank_times = models.IntegerField(null=True, default=0)
    delivery_mode = models.BooleanField(default=0)
    class Meta:
        managed = True
        db_table = 'customer'

class Delivery(models.Model):
    delivery_staff_id = models.ForeignKey(Customer, models.CASCADE)
    delivery_staff_rank = models.IntegerField(default=0)
    delivery_staff_rank_time = models.IntegerField(default=0)
    class Meta:
        managed = True
        db_table = 'delivery_staff'

class Restaurant(models.Model):
    restaurant_sireal = models.CharField(max_length=40, primary_key=True)
    restaurant_id = models.CharField(max_length=40)
    psw = models.CharField(max_length=20)
    Restaurant_name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    mail_address = models.CharField(max_length=150, null=True)
    lacation = models.CharField(max_length=45)
    total_rank = models.IntegerField(default=0)
    rank_times = models.IntegerField(default=0)
    class Meta:
        managed = True
        db_table = 'restaurant'

class Dishes(models.Model):
    dishes_id = models.CharField(max_length=20, primary_key=True)
    restaurant_id = models.ForeignKey(Restaurant , models.CASCADE)
    dishes_name = models.CharField(max_length=45)
    dishes_price = models.IntegerField()
    option = JSONField(null=True)
    class Meta:
        managed = True
        db_table = 'dishes'

class Order(models.Model):
    order_id = models.CharField(max_length=40, primary_key=True)
    order_items = JSONField()
    destination = models.CharField(max_length=250)
    status = models.BooleanField()
    price = models.IntegerField()
    customer_id = models.CharField(max_length=40)
    delivery_id = models.CharField(max_length=40)
    class Meta:
        managed = True
        db_table = 'order'