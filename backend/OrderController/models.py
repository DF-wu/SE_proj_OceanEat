from django.db import models

class OrderController(models.Model):
    order_id = models.TextField(primary_key=True)
    customer_id = models.TextField()
    delivery_id = models.TextField()
    # order_items = JSONField()
    order_items = models.TextField()
    destination = models.TextField()
    status = models.BinaryField()
    price = models.IntegerField()