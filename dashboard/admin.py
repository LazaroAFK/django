from django.contrib import admin
from .models import Almacenaje, Clientes, Datos, Generos, Marcas, Productos, Tipotarjeta

admin.site.register(Almacenaje)
admin.site.register(Clientes)
admin.site.register(Datos)
admin.site.register(Generos)
admin.site.register(Marcas)
admin.site.register(Productos)
admin.site.register(Tipotarjeta)