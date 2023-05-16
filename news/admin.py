from django.contrib import admin

from .models import Noticia, Comentario


@admin.register(Noticia)
class ProfileNews(admin.ModelAdmin):
    list_display = ('titulo', 'data_field', 'autor', 'fecha_publicacion')
    list_display_links = ('data_field',)

    search_fields = (
        'nombre',
        'autor',
        'fecha_publicacion'
    )