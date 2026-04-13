from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Libro, Orden  # ajusta a tus modelos

admin.site.register(Libro)
admin.site.register(Orden)