from django.contrib import admin

from zoo import models

admin.register(models.Cat)
admin.register(models.Dog)
admin.register(models.Animal)
admin.register(models.BigCat)
admin.register(models.Genus)
