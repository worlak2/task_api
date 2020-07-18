from django.contrib import admin

from client_api.models import Task, Client, Responsible

models_to_register = [Task, Client, Responsible]
admin.site.register(models_to_register)
