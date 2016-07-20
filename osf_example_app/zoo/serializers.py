from rest_framework import serializers

from zoo import models


class GenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genus
        fields = ('name', )


class AnimalSerializer(serializers.ModelSerializer):
    genus = GenusSerializer()

    class Meta:
        model = models.Animal
        fields = ('name', 'number', 'genus', 'animals_it_eats', )


class CatSerializer(AnimalSerializer):
    animals_it_eats = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='cat-detail',
        queryset=models.Cat.objects.all()
    )

    class Meta:
        model = models.Cat


class DogSerializer(AnimalSerializer):
    animals_it_eats = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='dog-detail',
        queryset=models.Animal.objects.all()
    )

    class Meta:
        model = models.Dog


class BigCatSerializer(CatSerializer):
    animals_it_eats = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='bigcat-detail',
        queryset=models.Animal.objects.all()
    )
    class Meta:
        model = models.BigCat
