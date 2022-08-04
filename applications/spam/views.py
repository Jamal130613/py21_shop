from django.shortcuts import render
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from applications.spam.models import Contact
from applications.spam.serializers import ContactSerializer


class ContactView(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

