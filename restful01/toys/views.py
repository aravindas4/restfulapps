from django.shortcuts import render
from rest_framework import generics

from toys import models as toys_models
from toys import serializers as toys_serializers


class ToyList(generics.ListCreateAPIView):
    queryset = toys_models.Toy.objects.all()
    serializer_class = toys_serializers.ToySerializer
    name = 'toy-list'


class ToyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = toys_models.Toy.objects.all()
    serializer_class = toys_serializers.ToySerializer
    name = 'toy-detail'
