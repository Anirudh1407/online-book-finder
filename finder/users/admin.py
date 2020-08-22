from django.contrib import admin
from django.apps import apps

# Register your models here.

app = apps.get_app_config('users')
admin.site.register(app.get_models())
