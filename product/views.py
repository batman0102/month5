from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Review, Category
from product.serializers import (ProductSerializer, ProductDetailSerializer,
                                 ReviewSerializer, ReviewsSerializer,
                                 CategorySerializer, CategoriesSerializer,
                                 ProductsReviewsSerializer)



@api_view(['GET', 'POST'])
def products_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        list_ = ProductSerializer(products, many=True).data
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            category_id=category_id,
        )
        return Response(status=status.HTTP_201_CREATED, data=ProductDetailSerializer(product).data)



@api_view(['GET', 'PUT', 'DELETE'])
def products_detail_api_view(request, id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        list_ = ProductDetailSerializer(products).data
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        products.title = request.data.get('title')
        products.description = request.data.get('description')
        products.price = request.data.get('price')
        products.category_id = request.data.get('category_id')
        return Response(status=status.HTTP_201_CREATED, data=ProductDetailSerializer(products).data)
    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        list_ = ReviewsSerializer(reviews, many=True).data
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        product_id = request.data.get('product_id')
        stars = request.data.get('stars')
        review = Review.objects.create(
            text=text,
            product_id=product_id,
            stars=stars
        )
        return Response(status=status.HTTP_201_CREATED, data=ReviewsSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        list_ = ReviewSerializer(reviews).data
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        reviews.text = request.data.get('text')
        reviews.product_id = request.data.get('product_id')
        reviews.stars = request.data.get('stars')
        return Response(status=status.HTTP_201_CREATED, data=ReviewSerializer(reviews).data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def categories_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        list_ = CategoriesSerializer(categories, many=True).data
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(
            name=name
        )
        return Response(status=status.HTTP_201_CREATED, data=CategoriesSerializer(category).data)

@api_view(['GET', 'PUT', 'DELETE'])
def category_api_view(request, id):
    try:
        categories = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        list_ = CategorySerializer(categories).data
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        categories.name = request.data.get('name')
        return Response(status=status.HTTP_201_CREATED, data=CategoriesSerializer(categories).data)
    elif request.method == 'DELETE':
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def products_reviews_api_view(request):
    products = Product.objects.all()
    list_ = ProductsReviewsSerializer(products, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)