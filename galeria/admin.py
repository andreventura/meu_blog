from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from models import Album, Imagem

class AdminAlbum(ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

class AdminImagem(ModelAdmin):
    list_display = ('album','titulo',)
    list_filter = ('album',)
    search_fields = ('titulo','descricao',)

admin.site.register(Album, AdminAlbum)
admin.site.register(Imagem, AdminImagem)

