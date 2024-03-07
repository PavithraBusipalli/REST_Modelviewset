from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
# Create your views here.

# queryset and serializer class are standard variables
class ProductCrud(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = Product_cat_ModelSerializer
