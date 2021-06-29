from django.contrib import admin

from .models import Equipment,Parameter,Var

admin.site.register(Equipment),
admin.site.register(Parameter),
admin.site.register(Var),