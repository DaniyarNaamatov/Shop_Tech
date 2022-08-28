from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, mixins
from rest_framework.filters import SearchFilter

from mag.models import Product, Reviews, Category
from mag.pagination import ProductAPIListPagination
from mag.serializers import *



class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']
    pagination_class = ProductAPIListPagination


class ProductAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # authentication_classes = (TokenAuthentication, )
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["title"]
    search_fields = ["title"]
    lookup_field = 'id'


class ReviewsView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author', 'text']
    search_fields = ['author', 'text']


class ReviewsAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author', 'text']
    search_fields = ['author', 'text']
    lookup_field = 'id'


