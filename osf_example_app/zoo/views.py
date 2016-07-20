from rest_framework import viewsets

from zoo import serializers
from zoo import models


class AnimalViewSet(viewsets.ModelViewSet):
    pass


class GenusViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GenusSerializer
    queryset = models.Genus.objects.all()


class DogViewSet(AnimalViewSet):
    serializer_class = serializers.DogSerializer
    queryset = models.Dog.objects.all()


class CatViewSet(AnimalViewSet):
    serializer_class = serializers.CatSerializer
    queryset = models.Cat.objects.all()


class BigCatViewSet(CatViewSet):
    serializer_class = serializers.BigCatSerializer
    queryset = models.BigCat.objects.all()
