from django.contrib import admin

from zoo import models

admin.site.register(models.Cat)
admin.site.register(models.Animal)
admin.site.register(models.Dog)
admin.site.register(models.BigCat)
admin.site.register(models.Genus)
