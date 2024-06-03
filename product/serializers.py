from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from product.models import Product, Review, Category


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product stars'.split()

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name products_count'.split()

    def get_products_count(self, obj):
        return obj.products.count()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()

class ProductsSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True)
    class Meta:
        model = Product
        fields = 'id title price reviews'.split()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title description price category_name'.split()

class ProductsReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True)
    class Meta:
        model = Product
        fields = 'id title price reviews average_rating'.split()

    def get_average_rating(self, obj):
        return obj.average_rating()

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=55)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(min_value=100, max_value=10000)
    category_id = serializers.IntegerField(min_value=1)

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except:
            raise ValidationError('Category does not exist')
        return category_id

class ReviewsValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=155)
    product_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except:
            raise ValidationError('Product does not exist')
        return product_id

class CategoriesValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=155)