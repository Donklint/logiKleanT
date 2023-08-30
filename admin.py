from django.contrib import admin
from .models import CustomerTable

models_list = [CustomerTable]
admin.site.register(models_list)


# Register your models here.
