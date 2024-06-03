from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from product.models import Product, Review, Category
from product.serializers import (ProductsSerializer, ProductSerializer,
                                 ReviewSerializer, ReviewsSerializer,
                                 CategorySerializer, CategoriesSerializer,
                                 ProductsReviewsSerializer, ProductValidateSerializer,
                                 ReviewsValidateSerializer, CategoriesValidateSerializer)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3


class ReviewsCreateListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    pagination_class = CustomPageNumberPagination

class ReviewItemListApi(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

class CategoriesCreateListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = CustomPageNumberPagination

class CategoryItemListApi(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class ProductsCreateListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = CustomPageNumberPagination

class ProductItemListApi(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProductsReviewsAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serialized_products = ProductsReviewsSerializer(products, many=True).data
        return Response(data=serialized_products, status=status.HTTP_200_OK)