from rest_framework import serializers
from product.models import Product, Review, Category


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text product stars'.split()

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name products_count'.split()

    def get_products_count(self, obj):
        return obj.products.count()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True)
    class Meta:
        model = Product
        fields = 'title price reviews'.split()

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title description price category_name'.split()

class ProductsReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True)
    class Meta:
        model = Product
        fields = 'title price reviews average_rating'.split()

    def get_average_rating(self, obj):
        return obj.average_rating()

