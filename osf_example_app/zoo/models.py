from __future__ import unicode_literals

from django.db import models

# Let's assume we have a zoo
from typedmodels.models import TypedModel


class Animal(TypedModel):
    name = models.CharField(max_length=255)  # max_length is required for CharFields
    number = models.PositiveIntegerField(verbose_name='a name that will appear in the admin')
    genus = models.ForeignKey('Genus')  # putting things in quotes allows you to use it without
                                                             # importing it or before you've defined it
    animals_it_eats = models.ManyToManyField('self', related_query_name='eaten_by', blank=True)
                                                      # ManyToManyField allows relations to multiple things
                                                      # self is a magic keyword that relates it to itself
                                                      # you could also specify an imported model or a model name in quotes
    def __str__(self):
        return self.name

    def __repr__(self):
        return u'<%s: %s>' % (self.__class__.__name__, self.name)

    class Meta:
        unique_together = ('name', 'genus')  # this will force name and genus to be unique together


class Genus(models.Model):
    name = models.CharField(max_length=255, blank=True)  # use blank=True for optional fields
    def __str__(self):
        return self.name

class Cat(Animal):
    # because Cat inherits from abstract Animal it will create it's own table with the fields from Animal and from Cat
    loudness = models.IntegerField()

class Dog(Animal):
    fuzzy = models.NullBooleanField()

class BigCat(Cat):
    # this can't have extra fields because it's data will go in the table for Cat

    # but it can have behavior
    @property
    def growl_size(self):
        return self.loudness

    class Meta:
        proxy = True
