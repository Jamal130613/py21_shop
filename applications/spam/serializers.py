from django.contrib.auth import get_user_model
from rest_framework import serializers
from applications.spam.models import Contact
from applications.spam.tasks import spam_email

User = get_user_model()


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.get(**validated_data)
        spam_email.delay(user.email)
        return user
