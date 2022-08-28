from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from mag.models import Product, Reviews, Category


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("title", "descriptions", "price", "cat")


class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"





class ProductValidateSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    descriptions = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    # category = serializers.IntegerField()

    @property
    def product_data_director(self):
        dict_ = {
            "title": self.validated_data.get("title"),
            "description": self.validated_data.get("description", ""),
            "price": self.validated_data.get("price", ""),
            "cat_id": self.validated_data.get("cat_id"),
        }
        return dict_


class ReviewsValidate(serializers.Serializer):
    author = serializers.CharField(max_length=255)
    text = serializers.CharField()
    product = serializers.IntegerField()

    @property
    def reviews_data_director(self):
        dict_1 = {
            "author": self.validated_data.get("author"),
            "text": self.validated_data.get("text", ""),
            "product_id": self.validated_data.get("product_id", ""),
        }
        return dict_1

    def validate_movie_id(self, product_id):
        if Reviews.objects.filter(id=product_id).count() == 0:
            raise ValidationError("Product not found")
        return product_id


