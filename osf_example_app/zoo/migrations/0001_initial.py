# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(b'zoo.cat', 'cat'), (b'zoo.dog', 'dog')], db_index=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('number', models.PositiveIntegerField(verbose_name='a name that will appear in the admin')),
                ('loudness', models.IntegerField(null=True)),
                ('fuzzy', models.NullBooleanField()),
                ('animals_it_eats', models.ManyToManyField(related_name='_animal_animals_it_eats_+', related_query_name='eaten_by', to='zoo.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='genus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoo.Genus'),
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('zoo.animal',),
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('zoo.animal',),
        ),
        migrations.AlterUniqueTogether(
            name='animal',
            unique_together=set([('name', 'genus')]),
        ),
        migrations.CreateModel(
            name='BigCat',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('zoo.cat',),
        ),
    ]
