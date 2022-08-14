from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import serializers
from applications.product.models import Category, Product, Image, Comment
from applications.product.tasks import send_product_info

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # print(representation)
        # representation['Hello'] = 'hello john'
        if not instance.parent:
            representation.pop('parent')
        return representation


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        requests = self.context.get('request')
        images = requests.FILES
        product = Product.objects.create(**validated_data)
        # user = User.objects.get(**validated_data)
        # spam_email_for_product.delay(user.email)

        for image in images.getlist('images'):
            Image.objects.create(product=product, image=image)

        send_product_info.delay(validated_data['name'])
        return product

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.likes.filter(like=True).count()
        rating_result = 0
        for rating in instance.ratings.all():
            rating_result += int(rating.rating)
        try:
            representation['rating'] = rating_result / instance.ratings.all().count()
        except ZeroDivisionError:
            # representation['rating'] = 0
            pass
        return representation


class RatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(required=True, min_value=1, max_value=5)


