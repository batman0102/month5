from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Review, Category
from product.serializers import (ProductSerializer, ProductDetailSerializer,
                                 ReviewSerializer, ReviewsSerializer,
                                 CategorySerializer, CategoriesSerializer,
                                 ProductsReviewsSerializer)



@api_view(['GET'])
def products_list_api_view(request):
    products = Product.objects.all()
    list_ = ProductSerializer(products, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def products_detail_api_view(request, id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    list_ = ProductDetailSerializer(products).data
    return Response(data=list_, status=status.HTTP_200_OK)

@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    list_ = ReviewsSerializer(reviews, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    list_ = ReviewSerializer(reviews).data
    return Response(data=list_, status=status.HTTP_200_OK)

@api_view(['GET'])
def categories_list_api_view(request):
    categories = Category.objects.all()
    list_ = CategoriesSerializer(categories, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_api_view(request, id):
    try:
        categories = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    list_ = CategorySerializer(categories).data
    return Response(data=list_, status=status.HTTP_200_OK)

@api_view(['GET'])
def products_reviews_api_view(request):
    products = Product.objects.all()
    list_ = ProductsReviewsSerializer(products, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)