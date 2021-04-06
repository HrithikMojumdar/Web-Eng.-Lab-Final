from django.contrib import admin
from.models import UserProfile, product, categories
# Register your models here.
 
admin.site.register(UserProfile)
admin.site.register(product)
admin.site.register(categories)