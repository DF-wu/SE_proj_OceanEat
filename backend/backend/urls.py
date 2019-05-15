"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from OceanEat import views
import  OceanEat

router = DefaultRouter()

# register OceanEat ViewSet (API)
router.register(r'Customer', views.CustomerViewSet)
router.register(r'Delivery', views.DeliveryViewSet)
router.register(r'Restaurant', views.RestaurantViewSet)
router.register(r'Dishes', views.DishesViewSet)

# For APIs
urlpatterns = [
    url(r'^api/', include(router.urls)),
]

# urlpatterns += [
#     re_path(r'(?P<path>.*)', TemplateView.as_view(template_name="index.html"))
# ]
