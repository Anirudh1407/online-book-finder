from django.contrib import admin
from django.apps import apps

# Register your models here.

app = apps.get_app_config('books')
admin.site.register(app.get_models())
